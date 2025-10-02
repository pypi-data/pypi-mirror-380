"""Module for ACADA data ingestion (onsite) into the BDMS system using the IngestionClient.

This module provides the IngestionClient class to manage the ingestion of ACADA data into the BDMS system.
It includes functionality for constructing FITS file paths, converting ACADA paths to Logical File Names (LFNs),
registering replicas in Rucio, extracting metadata and adding metadata to registered replicas. Furthermore, the Ingest class asynchronously
processes ACADA data using a process pool, managing file discovery, queuing, and distribution to worker processes for ingestion using a continuous
polling-based approach.
"""

import logging
import os
import threading
import time
from concurrent.futures import Future, ProcessPoolExecutor
from contextlib import ExitStack
from functools import partial
from multiprocessing import cpu_count
from pathlib import Path
from queue import Empty, Queue
from traceback import format_exception
from typing import NamedTuple, Optional, Union

from astropy.io import fits
from filelock import FileLock, Timeout
from prometheus_client import Counter, Gauge
from rucio.client.accountclient import AccountClient
from rucio.client.client import Client, DIDClient
from rucio.client.replicaclient import ReplicaClient
from rucio.client.rseclient import RSEClient
from rucio.client.ruleclient import RuleClient
from rucio.client.scopeclient import ScopeClient
from rucio.common.checksum import adler32
from rucio.common.exception import Duplicate, RucioException

from bdms.extract_fits_metadata import (
    extract_metadata_from_data,
    extract_metadata_from_headers,
)

LOGGER = logging.getLogger(__name__)

__all__ = ["IngestionClient", "FITSVerificationError", "Ingest", "IngestResult"]

INGEST_RUNNING_MESSAGE = "Another ingestion process is already running"
DETECTED_NEW_TRIGGER_FILE = "Detected new trigger file"
TRIGGER_SUFFIX = ".trigger"

# Prometheus Metrics for monitoring
N_TASKS_SUCCESS = Counter("n_tasks_success", "Number of successfully finished tasks.")
N_TASKS_FAILED = Counter("n_tasks_failed", "Number of failed tasks.")
N_TASKS_CANCELLED = Counter("n_tasks_cancelled", "Number of cancelled tasks.")
N_TASKS_SKIPPED = Counter("n_tasks_skipped", "Number of skipped tasks.")
N_TASKS_PROCESSED = Counter(
    "n_tasks_processed", "Total number of tasks processed by the Ingest daemon"
)
TASKS_IN_QUEUE = Gauge("n_tasks_queued", "Current number of queued tasks")
BYTES_INGESTED = Counter("bytes_ingested", "Total ingested file size")


class IngestResult(NamedTuple):
    """Result of the ingestion of a single file.

    Attributes
    ----------
    lfn : str
        The Logical File Name of the processed file.
    skipped : bool
        True if file was already ingested, False if newly processed.
    file_size : int
        Size of the file in bytes.
    """

    lfn: str
    skipped: bool
    file_size: int


class IngestionClient:
    """A client for BDMS ingestion and replication.

    This class provides methods to ingest ACADA data into the BDMS system, including converting ACADA paths to
    Logical File Names (LFNs), registering replicas in Rucio, extracting metadata and adding metadata to registered replicas, and
    replicating data to offsite RSEs.

    Parameters
    ----------
    data_path : str
        Path to data directory. This is a required argument.
    rse : str
        Rucio Storage Element (RSE) name. This is a required argument.
    vo : str, optional
        Virtual organization name prefix. Defaults to "ctao".
    logger : logging.Logger, optional
        Logger instance. If None, a new logger is created.
    scope : str, optional
        Rucio scope to use for replica registration. Defaults to 'acada'.

    Raises
    ------
    FileNotFoundError
        If the specified data directory does not exist.
    ValueError
        If the specified RSE is not available in Rucio.
    RuntimeError
        If there is an error communicating with Rucio while:

        - Checking RSE availability.
        - Initializing Rucio clients (related to configuration and authentication issues).
        - Managing the Rucio scope.
    """

    def __init__(
        self,
        data_path: Union[str, os.PathLike],
        rse: str,
        vo="ctao",
        logger=None,
        scope="acada",
    ) -> None:
        self.logger = logger or LOGGER.getChild(self.__class__.__name__)
        self.vo = vo

        if data_path is None:
            raise ValueError("data_path must be provided and cannot be None")

        # Set data path (Prefix)
        self.data_path = Path(data_path)
        if not self.data_path.is_dir():
            raise FileNotFoundError(f"Data directory not found at {self.data_path}")

        self.rse = rse

        # Check RSE availability before proceeding to next steps
        self._check_rse_availability()

        # Initialize Rucio clients
        try:
            self.client = Client()
            self.replica_client = ReplicaClient()
            self.scope_client = ScopeClient()
            self.account_client = AccountClient()
            self.rse_client = RSEClient()
            self.rule_client = RuleClient()
            self.did_client = DIDClient()
        except RucioException as e:
            self.logger.error("Failed to initialize Rucio clients: %s", str(e))
            raise

        # Set the scope and ensure it exists in Rucio
        self.scope = scope
        self.user = self.account_client.whoami()["account"]
        self._add_acada_scope()

    def _check_rse_availability(self) -> None:
        """Check if the specified RSE is available in Rucio.

        Raises
        ------
        ValueError
            If the RSE is not found in Rucio.
        rucio.common.exception.RucioException
            If there is an error communicating with Rucio (e.g., network issues, authentication errors).
        """
        rse_client = RSEClient()
        available_rses = [rse["rse"] for rse in rse_client.list_rses()]
        if self.rse not in available_rses:
            raise ValueError(
                f"RSE '{self.rse}' is not available in Rucio. Available RSEs: {available_rses}"
            )
        self.logger.info("RSE '%s' is available in Rucio", self.rse)

    def _add_acada_scope(self) -> None:
        """Add the specified scope to Rucio if it doesn't already exist.

        Raises
        ------
        RuntimeError
            If the scope cannot be created or managed in Rucio.
        """
        try:
            self.scope_client.add_scope(self.user, self.scope)
        except Duplicate:
            # Scope already exists
            return
        except RucioException as e:
            self.logger.error(
                "Failed to manage scope '%s' in Rucio: %s",
                self.scope,
                str(e),
            )
            raise

    def acada_to_lfn(self, acada_path) -> str:
        """Convert an ACADA path to a BDMS Logical File Name (LFN).

        Parameters
        ----------
        acada_path : str or Path
            The ACADA file path to convert.

        Returns
        -------
        str
            The generated BDMS LFN (e.g., '/ctao/acada/DL0/LSTN-01/events/YYYY/MM/DD/file.fits.fz').

        Raises
        ------
        ValueError
            If ``acada_path`` is not an absolute path or is not within the BDMS data path (prefix) or
            does not start with the expected '<vo>/<scope>' prefix under the data path.
        """
        acada_path = Path(acada_path)

        # Validate that the path is absolute
        if not acada_path.is_absolute():
            raise ValueError("acada_path must be absolute")

        # Validate that acada_path is within data_path
        try:
            rel_path = acada_path.relative_to(self.data_path)
        except ValueError:
            raise ValueError(
                f"acada_path {acada_path} is not within data_path {self.data_path}"
            )

        # Validate that acada_path starts with <vo>/<scope> under data_path
        expected_prefix = self.data_path / self.vo / self.scope
        if not acada_path.is_relative_to(expected_prefix):
            raise ValueError(
                f"acada_path {acada_path} must start with {expected_prefix} (vo: {self.vo}, scope: {self.scope})"
            )

        bdms_lfn = f"/{rel_path}"
        return bdms_lfn

    def check_replica_exists(self, lfn: str) -> bool:
        """Check if a replica already exists for the given LFN on the specified RSE.

        Parameters
        ----------
        lfn : str
            The Logical File Name (LFN) to check.


        Returns
        -------
        bool
            True if the replica exists and has a valid PFN, False otherwise.

        Raises
        ------
        RuntimeError
            If a replica exists but has no PFN for the RSE, indicating an invalid replica state.
        """
        replicas = list(
            self.replica_client.list_replicas(
                dids=[{"scope": self.scope, "name": lfn}],
                rse_expression=self.rse,
            )
        )

        self.logger.debug("Existing Replicas for lfn '%r'", replicas)
        if replicas:
            replica = replicas[0]
            pfns = replica["rses"].get(self.rse, [])
            if not pfns:
                raise RuntimeError(
                    f"No PFN found for existing replica with LFN {lfn} on {self.rse}"
                )
            return True
        return False

    def add_onsite_replica(self, acada_path: Union[str, Path]) -> IngestResult:
        """Register a file as a replica in Rucio on the specified RSE and return the ingestion result.

        Parameters
        ----------
        acada_path : str or Path
            The ACADA path where the file is located.

        Returns
        -------
        IngestResult
            Result of the replica registration.

        Raises
        ------
        FileNotFoundError
            If the file does not exist at ``acada_path``.
        RuntimeError
            In the following cases:
            - If a replica already exists but has no PFN for the RSE (raised by `check_replica_exists`).
            - If the replica registration fails (e.g., due to a Rucio server issue).
        """
        acada_path = Path(acada_path)
        self.logger.debug("Starting ingestion for path '%s'", acada_path)

        # Validate file existence
        if not acada_path.is_file():
            raise FileNotFoundError(f"File does not exist at {acada_path}")

        # Generate LFN
        lfn = self.acada_to_lfn(acada_path=str(acada_path))
        self.logger.info("Using LFN '%s' for path '%s'", lfn, acada_path)

        # Check if the replica already exists
        if self.check_replica_exists(lfn):
            self.logger.info("Replica already exists for lfn '%s', skipping", lfn)
            return IngestResult(lfn=lfn, skipped=True, file_size=0)

        # Proceed with registering the replica if check_replica_exists returns False
        valid, metadata = verify_and_extract_metadata(acada_path)
        metadata["valid_fits_checksum"] = valid

        # Compute rucio file metadata
        file_size = acada_path.stat().st_size
        checksum = adler32(acada_path)

        # Register the replica in Rucio
        try:
            success = self.replica_client.add_replica(
                rse=self.rse,
                scope=self.scope,
                name=lfn,
                bytes_=file_size,
                adler32=checksum,
            )
            if not success:
                raise RuntimeError(
                    f"Failed to register replica for LFN {lfn} on {self.rse}"
                )
        except Exception as e:
            raise RuntimeError(
                f"Failed to register replica for LFN {lfn} on {self.rse}: {str(e)}"
            )
        self.logger.info("Successfully registered the replica for lfn '%s'", lfn)

        if len(metadata) > 0:
            self.did_client.set_metadata_bulk(scope=self.scope, name=lfn, meta=metadata)
            self.logger.info("Set metadata of %r to %r", lfn, metadata)

        return IngestResult(lfn=lfn, skipped=False, file_size=file_size)

    def add_offsite_replication_rules(
        self,
        lfn: str,
        copies: int = 1,
        lifetime: Optional[int] = None,
        offsite_rse_expression: str = "OFFSITE",
    ) -> list[str]:
        """Replicate an already-ingested ACADA data product to offsite RSEs.

        This method assumes the data product has already been ingested into the onsite RSE and is identified by the given LFN.
        It creates one or two replication rules to offsite RSEs, depending on the number of copies requested:
        - First rule: Always creates exactly 1 replica to prevent parallel transfers from the onsite RSE.
        - Second rule (if copies > 1): Creates additional replicas (equal to the requested copies), sourcing data from offsite RSEs to avoid further transfers from the onsite RSE.

        Parameters
        ----------
        lfn : str
            The Logical File Name (LFN) of the already-ingested ACADA data product.
        copies : int, optional
            The total number of offsite replicas to create. Defaults to 1.
            - If copies == 1, only one rule is created with 1 replica.
            - If copies > 1, a second rule is created with the requested number of copies, sourcing from offsite RSEs.
        lifetime : int, optional
            The lifetime of the replication rules in seconds. If None, the rules are permanent.
        offsite_rse_expression : str, optional
            The RSE expression identifying offsite Rucio Storage Elements (RSEs). Defaults to "OFFSITE".

        Returns
        -------
        List[str]
            The list of replication rule IDs created (1 or 2 rules, depending on the copies parameter).

        Raises
        ------
        RuntimeError
            If there is an error interacting with Rucio, including:
            - Failure to create a new replication rule (e.g., DuplicateRule).
        """
        # Create the DID for replication
        did = {"scope": self.scope, "name": lfn}
        dids = [did]

        # Initialize the list of rule IDs
        rule_ids = []

        # First rule: Always create exactly 1 replica to prevent parallel transfers from onsite RSE
        try:
            rule_id_offsite_1 = self.rule_client.add_replication_rule(
                dids=dids,
                rse_expression=offsite_rse_expression,
                copies=1,
                lifetime=lifetime,
                source_replica_expression=None,  # Let Rucio choose the source (onsite RSE)
            )[0]
            self.logger.debug(
                "Created first replication rule %s for DID %s to RSE expression '%s' with 1 copy, lifetime %s",
                rule_id_offsite_1,
                did,
                offsite_rse_expression,
                lifetime if lifetime is not None else "permanent",
            )
            rule_ids.append(rule_id_offsite_1)
        except RucioException as e:
            self.logger.error(
                "Failed to create first offsite replication rule for DID %s to RSE expression '%s': %s",
                did,
                offsite_rse_expression,
                str(e),
            )
            raise

        # Second rule: If more than one copy is requested, create a second rule sourcing from offsite RSEs
        if copies > 1:
            # Exclude the onsite RSE to ensure the data is sourced from an offsite RSE
            # source_replica_expression = f"*\\{onsite_rse}" (we could also consider this expression)
            source_replica_expression = offsite_rse_expression
            self.logger.debug(
                "Creating second offsite replication rule to RSE expression '%s' with %d copies, sourcing from offsite RSEs",
                offsite_rse_expression,
                copies,
            )
            try:
                rule_id_offsite_2 = self.rule_client.add_replication_rule(
                    dids=dids,
                    rse_expression=offsite_rse_expression,
                    copies=copies,  # Use requested number of copies
                    lifetime=lifetime,
                    source_replica_expression=source_replica_expression,
                )[0]
                self.logger.debug(
                    "Created second replication rule %s for DID %s to RSE expression '%s' with %d copies, source_replica_expression '%s', lifetime %s",
                    rule_id_offsite_2,
                    did,
                    offsite_rse_expression,
                    copies,
                    source_replica_expression,
                    lifetime if lifetime is not None else "permanent",
                )
                rule_ids.append(rule_id_offsite_2)
            except RucioException as e:
                self.logger.error(
                    "Failed to create second offsite replication rule for DID %s to RSE expression '%s': %s",
                    did,
                    offsite_rse_expression,
                    str(e),
                )
                raise

        self.logger.info(
            "Created %d offsite replication rule(s) for LFN '%s' to RSE expression '%s': %s",
            len(rule_ids),
            lfn,
            offsite_rse_expression,
            rule_ids,
        )
        return rule_ids


class FITSVerificationError(Exception):
    """Raised when a FITS file does not pass verification."""


def verify_fits_checksum(hdul: fits.HDUList):
    """
    Verify all present checksums in the given HDUList.

    Goes through all HDUs and verifies DATASUM and CHECKSUM if
    present in the given HDU.

    Verifies DATASUM before CHECKSUM to distinguish failure
    in data section vs. failure in header section.

    Raises
    ------
    FITSVerificationError: in case any of the checks are not passing
    """
    for pos, hdu in enumerate(hdul):
        name = hdu.name or ""

        checksum_result = hdu.verify_checksum()
        if checksum_result == 0:
            msg = f"CHECKSUM verification failed for HDU {pos} with name {name!r}"
            raise FITSVerificationError(msg)
        elif checksum_result == 2 and pos != 0:  # ignore primary for warning
            LOGGER.warning("No CHECKSUM in HDU %d with name %r", pos, name)


def verify_and_extract_metadata(fits_path):
    """Verify checksums and extract metadata from FITS files.

    This wrapper transforms exceptions into log errors and minimizes
    the number of times the FITS file has to be opened.
    """
    # this context manager allows elegant handling
    # of conditionally present context managers
    # which allows better handling of exceptions below
    context = ExitStack()
    metadata = {}
    with context:
        try:
            hdul = context.enter_context(fits.open(fits_path))
        except Exception as e:
            LOGGER.error("Failed to open FITS file %r: %s", fits_path, e)
            return False, metadata

        try:
            verify_fits_checksum(hdul)
        except FITSVerificationError as e:
            LOGGER.error("File %r failed FITS checksum verification: %s", fits_path, e)
            return False, metadata

        try:
            metadata = extract_metadata_from_headers(hdul)
            metadata.update(extract_metadata_from_data(fits_path))
            return True, metadata
        except Exception as e:
            LOGGER.error("Failed to extract metadata from %r: %s", fits_path, e)
            return False, metadata


def process_file(
    client: IngestionClient, file_path: str, logger=None, copies: int = 2
) -> IngestResult:
    """Process a single file with IngestionClient, clean up the trigger file, and return the ingestion result.

    Parameters
    ----------
    client : IngestionClient
        The IngestionClient instance to handle replica registration and replication.
    file_path : str
        The path to the file to process.
    logger : logging.Logger, optional
        Logger instance. If None, uses the client's logger or a default logger.
    copies: int
        The number of offsite copies to create. Defaults to 2.

    Returns
    -------
    IngestResult
        Result of the ingestion process.
    """
    logger = logger or LOGGER.getChild("Ingest")

    result = client.add_onsite_replica(file_path)

    if not result.skipped:
        client.add_offsite_replication_rules(result.lfn, copies=copies)

    trigger_file = Path(file_path + TRIGGER_SUFFIX)
    if trigger_file.exists():
        trigger_file.unlink()
        logger.debug("Removed trigger file %s", trigger_file)

    return result


class Ingest:
    """Ingestion daemon service to process ACADA data products using a process pool with result handling.

    Monitors a specified directory for trigger files using a polling loop,
    submitting each file for ingestion to a ProcessPoolExecutor for parallel processing.
    Uses an improved callback-based result handling system with structured task tracking
    and immediate result processing. The daemon ensures compatibility with shared
    filesystems through polling and prevents multiple instances using a lock file.
    """

    def __init__(
        self,
        client,
        top_dir: Union[str, Path],
        num_workers: int = cpu_count(),
        lock_file_path: Union[str, Path, None] = None,
        polling_interval: float = 1.0,
        check_interval: float = 1.0,
        offsite_copies: int = 2,
    ) -> None:
        """Initialize the ingestion daemon with configuration parameters.

        Sets up the client, directory, worker count, intervals, and initializes
        a process-safe queue and daemon state.
        """
        self.logger = LOGGER.getChild(self.__class__.__name__)
        self.stop_event = threading.Event()

        self.client = client

        self.top_dir = Path(top_dir)

        self.lock_file_path = (
            Path(lock_file_path)
            if lock_file_path is not None
            else self.top_dir / "bdms_ingest.lock"
        )
        # Lock instance to be held during entire daemon execution
        self.lock = FileLock(self.lock_file_path, timeout=10, thread_local=False)

        self.polling_interval = polling_interval
        self.check_interval = check_interval
        self.offsite_copies = offsite_copies

        self.num_workers = num_workers
        self.executor = None
        self.result_thread = None
        self.polling_thread = None

        # Result handling
        self.result_queue = Queue()
        self.task_counter = 0
        self.submitted_tasks = {}  # Track submitted tasks: {task_id: file_path}

        # Track already processed triggers
        self.known_triggers = set()

    def _done_callback(self, future, task_id: int, file_path: str):
        """Queue completed task result for processing.

        This method is invoked immediately when a worker process finishes
        processing a file. It queues the result for processing by the
        dedicated result handling thread.

        Parameters
        ----------
        future : concurrent.futures.Future
            The completed Future object containing the task result.
        task_id : int
            Unique identifier for the completed task.
        file_path : str
            Path to the file that was processed.
        """
        self.result_queue.put((task_id, file_path, future))

    def _submit_file(self, file_path: str):
        """Submit a file for processing using the callback pattern.

        Creates a unique task ID, submits the file to the worker pool, and
        sets up an immediate callback for result processing

        Parameters
        ----------
        file_path : str
            Path to the data file to be processed.
        """
        task_id = self.task_counter
        self.task_counter += 1

        self.submitted_tasks[task_id] = file_path

        # Update max concurrent tasks tracking
        current_concurrent = len(self.submitted_tasks)

        # Increment queue counter when task is submitted
        TASKS_IN_QUEUE.inc()

        self.logger.debug(
            "Submitting task %d for file %s (concurrent: %d)",
            task_id,
            file_path,
            current_concurrent,
        )

        future = self.executor.submit(
            process_file,
            self.client,
            file_path,
            logger=self.logger,
            copies=self.offsite_copies,
        )
        future.add_done_callback(
            partial(self._done_callback, task_id=task_id, file_path=file_path)
        )

    def _scan_for_triggers(self):
        """Scan directory for new .trigger files and submit them for processing."""
        # Find all .trigger files in the directory
        self.logger.info("Starting scan for new trigger files")
        start_time = time.time()
        current_triggers = set(self.top_dir.rglob("*.trigger"))
        scan_time = time.time() - start_time
        self.logger.debug(
            "Found %d trigger files in %.2fs", len(current_triggers), scan_time
        )

        # Find new triggers that we have not seen before
        new_triggers = current_triggers.difference(self.known_triggers)

        # Find triggers that disappeared (processed and deleted)
        disappeared_triggers = self.known_triggers.difference(current_triggers)

        self.logger.info(
            "Scanned for triggers: found %d total, %d new, %d disappeared",
            len(current_triggers),
            len(new_triggers),
            len(disappeared_triggers),
        )

        # Process new trigger files
        for trigger_file in new_triggers:
            self._process_trigger_file(trigger_file)

        # Update known_triggers to match currently existing trigger files
        self.known_triggers = current_triggers

    def _process_trigger_file(self, trigger_file: Path):
        """Process a trigger file by submitting its data file for ingestion."""
        data_file = trigger_file.with_suffix("")

        # pathological case of a link just called ".trigger"
        if trigger_file.name == TRIGGER_SUFFIX:
            self.logger.error(
                "Ignoring trigger file: %s, empty data file name", trigger_file
            )
            return

        if not data_file.exists():
            self.logger.error(
                "Ignoring trigger file: %s, data path %s missing",
                trigger_file,
                data_file,
            )
            return

        if not data_file.is_file():
            self.logger.error(
                "Ignoring trigger file: %s, data path %s is not a file",
                trigger_file,
                data_file,
            )
            return

        self.logger.info(
            "Processing trigger file %s, submitting data file %s",
            trigger_file,
            data_file,
        )

        try:
            self._submit_file(str(data_file))
        except Exception:
            self.logger.exception(
                "Failed to submit data file %s for processing", data_file
            )
            return

        self.logger.debug("Successfully processed trigger %s", trigger_file)

    def _polling_loop(self):
        """Continuously scan for trigger files until daemon stops."""
        self.logger.info(
            "Starting polling of directory %s every %.1f seconds",
            self.top_dir,
            self.polling_interval,
        )

        while not self.stop_event.is_set():
            try:
                self._scan_for_triggers()
            except Exception:
                self.logger.exception("Exception in polling loop")

            self.stop_event.wait(self.polling_interval)

        self.logger.info("Stopped polling for new trigger files")

    def _process_results(self):
        """Process results from the result queue.

        This method runs in a separate daemon thread and continuously processes
        completed tasks from the result queue. It handles task cleanup, result
        logging, and error reporting. The method implements the improved result
        handling pattern with structured error handling and performance tracking.

        The thread processes results until the stop_event is set and the queue
        is empty, ensuring all results are handled before shutdown.
        """
        self.logger.info("Result processing thread started")

        while not self.stop_event.is_set() or not self.result_queue.empty():
            try:
                task_id, file_path, future = self.result_queue.get(
                    timeout=self.check_interval
                )
            except Empty:
                continue

            try:
                self._handle_result(task_id, file_path, future)
            except Exception as e:
                self.logger.exception(
                    "Error processing result for task %d: %s", task_id, str(e)
                )

        self.logger.info("Result processing thread stopped")

    def _handle_result(
        self,
        task_id: int,
        file_path: str,
        future: Future,
    ) -> None:
        """Handle the result of a completed task.

        This method processes the result of a completed ingestion task, performs
        cleanup of task tracking data, calculates processing statistics for prometheus
        metrics, and logs the outcome.

        It handles successful completion, cancellation, and error cases.

        Parameters
        ----------
        task_id : int
            Unique identifier for the completed task.
        file_path : str
            Path to the file that was processed.
        future : concurrent.futures.Future
            The completed Future object containing the task result.
        """
        # Clean up task tracking
        path = self.submitted_tasks.pop(task_id, None)
        current_concurrent = len(self.submitted_tasks)
        TASKS_IN_QUEUE.dec()  # Always decrement queue counter

        self.logger.debug(
            "Task %d completed, remaining concurrent: %d",
            task_id,
            current_concurrent,
        )

        # Process the result
        # the order here is important, as the methods on the future object
        # raise if the future is in the wrong state
        if future.cancelled():
            status = "cancelled"
            N_TASKS_CANCELLED.inc()

        elif (e := future.exception()) is not None:
            self.logger.error(
                "Task %d for path %s failed: %s",
                task_id,
                path,
                "".join(format_exception(type(e), e, e.__traceback__)),
            )
            status = "failed"
            N_TASKS_FAILED.inc()
        else:
            result = future.result()
            if not result.skipped:
                status = "success"
                N_TASKS_SUCCESS.inc()
                BYTES_INGESTED.inc(result.file_size)
            else:
                status = "skipped"
                N_TASKS_SKIPPED.inc()

        N_TASKS_PROCESSED.inc()
        self.logger.info("Processed file %s with result %s.", file_path, status)

    def _check_directory(self) -> None:
        """Check if the directory is readable.

        Raises
        ------
        RuntimeError
            If the top directory is not accessible.
        """
        if not self.top_dir.is_dir() or not os.access(self.top_dir, os.R_OK):
            self.logger.error("Cannot read directory %s", self.top_dir)
            raise RuntimeError(f"Cannot read directory {self.top_dir}")

    def run(self, block=True) -> None:
        """Run the ingestion daemon, submitting file ingestion tasks to a process pool, and result handling.

        Initializes and runs the complete ingestion system including:

        1. Process checks (lock file acquisition and hold for entire runtime)
        2. Validates directory access
        3. Result processing thread startup
        4. Worker process pool creation
        5. File system monitoring with polling loop
        6. Graceful shutdown handling

        The method blocks until a shutdown signal is received (KeyboardInterrupt)
        or the stop_event is set. All components are properly shut down and
        cleaned up before the method returns.

        Parameters
        ----------
        block : bool
            If True (the default), this function will block forever
            running the ingest until another thread sets the stop event.
            If block is false, this function will return once ingest
            is running.
            In this case, the caller has to make sure to call the shutdown
            method to stop threads and worker processes and free the corresponding
            resources.

        Raises
        ------
        RuntimeError
            If another ingestion process is running or the directory is unreadable.
        """
        self._check_directory()

        # Acquire lock for the entire daemon execution, preventing multiple instances
        try:
            # Acquire the lock - this will be held for the entire daemon runtime
            self.lock.acquire(poll_interval=0.1)
            self.logger.info("Acquired lock file: %s", self.lock.lock_file)
        except Timeout:
            raise RuntimeError(INGEST_RUNNING_MESSAGE)

        # Write PID to the original lock file for reference
        self.lock_file_path.write_text(str(os.getpid()))
        self.logger.info("Written PID %d to %s", os.getpid(), self.lock_file_path)

        self._start_threads_and_worker_pool()

        if not block:
            return

        try:
            self.stop_event.wait(timeout=None)
        finally:
            self.shutdown()

    def _start_threads_and_worker_pool(self):
        """Start the ingestion by starting threads and worker pool."""
        self.stop_event.clear()

        if self.result_thread is not None:
            raise ValueError("Ingest is already running")

        # Start the result processing thread
        self.result_thread = threading.Thread(target=self._process_results)
        self.polling_thread = threading.Thread(target=self._polling_loop)

        self.result_thread.start()

        self.executor = ProcessPoolExecutor(max_workers=self.num_workers)
        self.logger.info("Started process pool with %d workers", self.num_workers)
        self.polling_thread.start()

    def shutdown(self):
        """Stop ingesting."""
        self.logger.info("Shutting down ingest.")
        self.stop_event.set()

        # shutdown the poller first, so we don't queue more files for ingestion
        if self.polling_thread is not None and self.polling_thread.is_alive():
            self.logger.info("Stopping Polling thread")
            self.polling_thread.join(timeout=30.0)
            if self.polling_thread.is_alive():
                self.logger.warning("File polling did not shutdown within 30s0")
            else:
                self.logger.info("Polling thread stopped")
        else:
            self.logger.info("Polling thread was not running")
        self.polling_thread = None

        # next shutdown the pool, we cancel all jobs not yet started but
        # wait for running ones to finish
        if self.executor is not None:
            self.logger.info("Stopping process pool")
            self.executor.shutdown(wait=True, cancel_futures=True)
            self.logger.info("Process pool stopped")
            self.executor = None

        # last, shutdown the reporting thread.
        if self.result_thread is not None and self.result_thread.is_alive():
            self.logger.info("Stopping result processing thread")
            self.result_thread.join()
        else:
            self.logger.info("Result processing thread was not running")
        self.result_thread = None

        if self.lock.is_locked:
            self.lock.release()
            if self.lock_file_path.exists():
                self.lock_file_path.unlink()
            self.logger.info("Released lock file: %s", self.lock_file_path)
        else:
            self.logger.info("Lock was not held")
        self.logger.info("Stopped ingestion daemon")
