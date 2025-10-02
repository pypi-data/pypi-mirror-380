"""Tests for onsite ingestion and replication into the BDMS system using the IngestionClient.

This module contains tests for the IngestionClient class, focusing on the conversion of ACADA paths to Logical File Names (LFNs), the registration of replicas in Rucio,
and the replication of data between Rucio storage elements (RSEs).
"""

import logging
import os
import secrets
import shutil
import subprocess
import threading
import time
import uuid
from concurrent.futures import Future
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen

import numpy as np
import pytest
from astropy.io import fits
from astropy.table import Table
from rucio.client import Client
from rucio.client.downloadclient import DownloadClient
from rucio.client.replicaclient import ReplicaClient
from rucio.client.ruleclient import RuleClient
from rucio.common.checksum import adler32
from rucio.common.exception import RucioException

from bdms.acada_ingestion import (
    TRIGGER_SUFFIX,
    Ingest,
    IngestionClient,
    process_file,
)
from bdms.tests.conftest import deployment_scale
from bdms.tests.utils import (
    reset_xrootd_permissions,
    wait_for_replicas,
    wait_for_replication_status,
    wait_for_trigger_file_removal,
)

LOGGER = logging.getLogger(__name__)

ONSITE_RSE = "STORAGE-1"
OFFSITE_RSE_1 = "STORAGE-2"
OFFSITE_RSE_2 = "STORAGE-3"

TEST_FILE_TRIGGER = "test_file.trigger"
RNG = np.random.default_rng(seed=42)


def setup_ingest(data_root_dir, vo, scope, top_dir, lock_base_path, num_workers=1):
    ingestion_client = IngestionClient(
        data_path=data_root_dir,
        rse=ONSITE_RSE,
        vo=vo,
        scope=scope,
    )
    return Ingest(
        client=ingestion_client,
        top_dir=top_dir,
        num_workers=num_workers,
        lock_file_path=lock_base_path / "bdms_ingest.lock",
        polling_interval=0.5,
        check_interval=0.5,
    )


def test_shared_storage(storage_mount_path: Path):
    """Test that the shared storage path is available."""

    msg = f"Shared storage {storage_mount_path} is not available on the client"
    assert storage_mount_path.exists(), msg


def trigger_judge_repairer() -> None:
    """Trigger the rucio-judge-repairer daemon to run once and fix any STUCK rules."""

    try:
        cmd = [
            ".toolkit/bin/kubectl",
            "exec",
            "deployment/bdms-rucio-daemons-judge-evaluator",
            "--",
            "/usr/local/bin/rucio-judge-repairer",
            "--run-once",
        ]
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True,
        )
        LOGGER.info("Triggered rucio-judge-repairer daemon: %s", result.stdout)
    except FileNotFoundError as e:
        LOGGER.error("kubectl command not found: %s", str(e))
        raise RuntimeError(
            "kubectl command not found. Ensure kubectl is in the PATH or working directory."
        ) from e
    except subprocess.CalledProcessError as e:
        LOGGER.error("Failed to trigger rucio-judge-repairer daemon: %s", e.stderr)
        raise


def test_acada_to_lfn(storage_mount_path: Path, test_vo: str):
    """Test the acada_to_lfn method of IngestionClient with valid and invalid inputs."""

    ingestion_client = IngestionClient(storage_mount_path, ONSITE_RSE, vo=test_vo)

    # Test Case 1: valid acada_path
    acada_path = (
        f"{ingestion_client.data_path}/{ingestion_client.vo}/{ingestion_client.scope}/DL0/LSTN-01/events/2023/10/13/"
        "Subarray_SWAT_sbid008_obid00081_0.fits.fz"
    )

    expected_lfn = (
        f"/{ingestion_client.vo}/{ingestion_client.scope}/DL0/LSTN-01/events/2023/10/13/"
        "Subarray_SWAT_sbid008_obid00081_0.fits.fz"
    )
    lfn = ingestion_client.acada_to_lfn(acada_path=acada_path)

    msg = f"Expected {expected_lfn}, got {lfn}"
    assert lfn == expected_lfn, msg

    # Test Case 2: Non-absolute acada_path (empty string)
    with pytest.raises(ValueError, match="acada_path must be absolute"):
        ingestion_client.acada_to_lfn(acada_path="")

    # Test Case 3: Non-absolute acada_path (relative path)
    with pytest.raises(ValueError, match="acada_path must be absolute"):
        ingestion_client.acada_to_lfn(acada_path="./test.fits")

    # Test Case 4: acada_path not within data_path
    invalid_acada_path = "/invalid/path/file.fits.fz"
    with pytest.raises(ValueError, match="is not within data_path"):
        ingestion_client.acada_to_lfn(acada_path=invalid_acada_path)

    # Test Case 5: acada_path does not start with <vo>/<scope>
    wrong_prefix_path = (
        f"{ingestion_client.data_path}/wrong_vo/wrong_scope/DL0/LSTN-01/file.fits.fz"
    )
    with pytest.raises(ValueError, match="must start with"):
        ingestion_client.acada_to_lfn(acada_path=wrong_prefix_path)

    # Test Case 6: acada_path starts with <vo> but wrong <scope>
    wrong_scope_path = f"{ingestion_client.data_path}/{ingestion_client.vo}/wrong_scope/DL0/LSTN-01/file.fits.fz"
    with pytest.raises(ValueError, match="must start with"):
        ingestion_client.acada_to_lfn(acada_path=wrong_scope_path)


@pytest.mark.usefixtures("_auth_proxy")
def test_check_replica_exists(
    storage_mount_path: Path,
    test_scope: str,
    onsite_test_file: tuple[Path, str],
    test_vo: str,
):
    """Test the check_replica_exists method of IngestionClient."""

    ingestion_client = IngestionClient(
        data_path=storage_mount_path,
        rse=ONSITE_RSE,
        vo=test_vo,
        scope=test_scope,
    )

    acada_path, _ = onsite_test_file

    # Generate the LFN
    lfn = ingestion_client.acada_to_lfn(acada_path)

    # Test Case 1: No replica exists yet
    msg = f"Expected no replica for LFN {lfn} before registration"
    assert not ingestion_client.check_replica_exists(lfn), msg

    # Register the replica in Rucio
    ingestion_client.add_onsite_replica(acada_path)

    # Test Case 2: Replica exists with a valid PFN
    msg = f"Expected replica to exist for LFN {lfn} after registration"
    assert ingestion_client.check_replica_exists(lfn), msg

    # Test Case 3: Non-existent LFN
    nonexistent_lfn = lfn + ".nonexistent"
    msg = f"Expected no replica for nonexistent LFN {nonexistent_lfn}"
    assert not ingestion_client.check_replica_exists(nonexistent_lfn), msg


@pytest.fixture
def file_location(request):
    return request.getfixturevalue(request.param)


@pytest.mark.parametrize(
    ("file_location", "metadata_dict"),
    [
        (
            "subarray_test_file",
            {
                "observatory": "CTA",
                "start_time": "2025-02-04T21:34:05",
                "end_time": "2025-02-04T21:43:12",
                "subarray_id": 0,
                "sb_id": 2000000066,
                "obs_id": 2000000200,
            },
        ),
        (
            "tel_trigger_test_file",
            {
                "observatory": "CTA",
                "start_time": "2025-02-04T21:34:05",
                "end_time": "2025-02-04T21:43:11",
                "tel_ids": [1],
                "sb_id": 2000000066,
                "obs_id": 2000000200,
            },
        ),
        (
            "tel_events_test_file",
            {
                "observatory": "CTA",
                "start_time": "2025-04-01T15:25:02",
                "end_time": "2025-04-01T15:25:03",
                "sb_id": 0,
                "obs_id": 0,
            },
        ),
    ],
    indirect=["file_location"],
)
@pytest.mark.usefixtures("_auth_proxy")
@pytest.mark.verifies_usecase("UC-110-1.1.1")
def test_add_onsite_replica_with_minio_fits_file(
    file_location: str,
    metadata_dict: dict,
    test_scope: str,
    tmp_path: Path,
    storage_mount_path,
    test_vo: str,
    caplog,
):
    """Test the add_onsite_replica method of IngestionClient using a dummy file."""

    ingestion_client = IngestionClient(
        data_path=storage_mount_path,
        rse=ONSITE_RSE,
        vo=test_vo,
        scope=test_scope,
    )

    filename = str(file_location).split("/")[-1]
    acada_path = storage_mount_path / test_vo / test_scope / filename
    acada_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(file_location, str(acada_path))
    reset_xrootd_permissions(storage_mount_path)

    # Use add_onsite_replica to register the replica
    lfn, skipped, size = ingestion_client.add_onsite_replica(acada_path=acada_path)
    assert size == os.stat(acada_path).st_size

    # Verify the LFN matches the expected LFN
    expected_lfn = ingestion_client.acada_to_lfn(acada_path)
    msg = f"Expected LFN {expected_lfn}, got {lfn}"
    assert lfn == expected_lfn, msg

    msg = "Expected the file to be newly ingested, but it was skipped"
    assert not skipped, msg

    # Download the file using the LFN
    download_spec = {
        "did": f"{ingestion_client.scope}:{lfn}",
        "base_dir": str(tmp_path),
        "no_subdir": True,
    }
    download_client = DownloadClient()
    download_client.download_dids([download_spec])

    # Verify the downloaded file
    download_path = tmp_path / lfn.lstrip("/")
    msg = f"Download failed at {download_path}"
    assert download_path.is_file(), msg

    msg = "Downloaded file content does not match the original."
    assert adler32(download_path) == adler32(file_location), msg

    # Check for don't ingest again if its already registered
    caplog.clear()
    lfn_check, skipped_check, size = ingestion_client.add_onsite_replica(
        acada_path=acada_path
    )
    msg = f"LFN mismatch on second ingestion attempt: expected {lfn}, got {lfn_check}"
    assert lfn_check == lfn, msg
    assert size == 0, "Expected size 0 for skipped file"

    msg = (
        "Expected the file to be skipped on second ingestion, but it was ingested again"
    )
    assert skipped_check, msg

    msg = f"'Replica already exists for lfn '{lfn}', skipping' in caplog records"
    assert f"Replica already exists for lfn '{lfn}', skipping" in [
        r.message for r in caplog.records
    ], msg

    # Retrieve metadata using the DIDClient
    did_client = Client()
    retrieved_metadata = did_client.get_metadata(
        scope=ingestion_client.scope, name=lfn, plugin="JSON"
    )

    # Verify the metadata matches the expected metadata
    for key, value in metadata_dict.items():
        msg = (
            f"Metadata mismatch for key '{key}'. "
            f"Expected: {value}, Got: {retrieved_metadata.get(key)}"
        )
        assert retrieved_metadata.get(key) == value, msg


def test_rses():
    """Test that the expected RSEs are configured."""
    client = Client()
    result = list(client.list_rses())

    rses = [r["rse"] for r in result]
    msg = f"Expected RSE {ONSITE_RSE} not found in {rses}"
    assert ONSITE_RSE in rses, msg

    msg = f"Expected RSE {OFFSITE_RSE_1} not found in {rses}"
    assert OFFSITE_RSE_1 in rses, msg

    msg = f"Expected RSE {OFFSITE_RSE_2} not found in {rses}"
    assert OFFSITE_RSE_2 in rses, msg


@pytest.fixture
def pre_existing_lfn(
    onsite_test_file: tuple[Path, str],
    test_scope: str,
    test_vo: str,
) -> str:
    """Fixture to provide an LFN for a replica pre-registered in Rucio without using IngestionClient."""

    # Construct the LFN manually based on the test file and scope
    acada_path, _ = onsite_test_file
    relative_path = str(acada_path).split(f"{test_vo}/{test_scope}/", 1)[-1]
    lfn = f"/{test_vo}/{test_scope}/{relative_path}"
    checksum = adler32(acada_path)

    # Construct the DID
    did = {"scope": test_scope, "name": lfn}

    # Register the replica directly using ReplicaClient
    replica_client = ReplicaClient()
    replica = {
        "scope": test_scope,
        "name": lfn,
        "bytes": acada_path.stat().st_size,  # File size
        "adler32": checksum,
    }
    try:
        replica_client.add_replicas(rse=ONSITE_RSE, files=[replica])
    except RucioException as e:
        LOGGER.error(
            "Failed to pre-register replica for LFN %s on %s: %s",
            lfn,
            ONSITE_RSE,
            str(e),
        )
        raise

    # Verify the replica is registered
    replicas = list(replica_client.list_replicas(dids=[did]))
    msg = f"Failed to verify pre-registration of replica for LFN {lfn} on {ONSITE_RSE}"
    assert replicas, msg

    return lfn


@pytest.mark.usefixtures("_auth_proxy")
@pytest.mark.verifies_usecase("UC-110-1.6")
def test_add_offsite_replication_rules(
    pre_existing_lfn: str,
    test_scope: str,
    test_vo: str,
    storage_mount_path: Path,
    tmp_path: Path,
    onsite_test_file: tuple[Path, str],
):
    """Test the add_offsite_replication_rules method of IngestionClient."""

    ingestion_client = IngestionClient(
        data_path=storage_mount_path,
        rse=ONSITE_RSE,
        vo=test_vo,
        scope=test_scope,
    )

    # Replicate the ACADA file to two offsite RSEs
    lfn = pre_existing_lfn
    did = {"scope": test_scope, "name": lfn}

    _, test_file_content = onsite_test_file  # Get the test file content

    offsite_rse_expression = "OFFSITE"
    copies = 2
    rule_ids = ingestion_client.add_offsite_replication_rules(
        lfn=lfn,
        offsite_rse_expression=offsite_rse_expression,
        copies=copies,
        lifetime=None,
    )

    rule_id_offsite_1 = rule_ids[0]
    rule_id_offsite_2 = rule_ids[1]
    rule_client = RuleClient()

    # Wait for the first offsite rule to complete (OFFSITE_RSE_1)
    wait_for_replication_status(rule_client, rule_id_offsite_1, expected_status="OK")

    # Verify the replica exists on either OFFSITE_RSE_1 or OFFSITE_RSE_2 after the first rule
    replica_client = ReplicaClient()
    replicas = next(replica_client.list_replicas(dids=[did]))
    states = replicas.get("states", {})
    msg = f"Expected replica on either {OFFSITE_RSE_1} or {OFFSITE_RSE_2} to be AVAILABLE after first rule: {states}"
    assert (
        states.get(OFFSITE_RSE_1) == "AVAILABLE"
        or states.get(OFFSITE_RSE_2) == "AVAILABLE"
    ), msg

    # Manually trigger the judge-repairer to ensure the second rule doesn't get stuck
    trigger_judge_repairer()

    # Wait for the second offsite rule to complete (OFFSITE_RSE_2)
    wait_for_replication_status(rule_client, rule_id_offsite_2, expected_status="OK")

    # Verify the replica exists on all RSEs
    replicas = next(replica_client.list_replicas(dids=[did]))
    states = replicas.get("states", {})
    LOGGER.info(
        "Replica states for DID %s in test_replicate_acada_data_to_offsite: %s",
        did,
        states,
    )

    msg = f"Expected replica on {ONSITE_RSE} to be AVAILABLE: {states}"
    assert states.get(ONSITE_RSE) == "AVAILABLE", msg

    msg = f"Expected replica on {OFFSITE_RSE_1} to be AVAILABLE: {states}"
    assert states.get(OFFSITE_RSE_1) == "AVAILABLE", msg

    msg = f"Expected replica on {OFFSITE_RSE_2} to be AVAILABLE: {states}"
    assert states.get(OFFSITE_RSE_2) == "AVAILABLE", msg

    # Download the file from OFFSITE_RSE_2 to verify its content
    download_spec = {
        "did": f"{test_scope}:{lfn}",
        "base_dir": str(tmp_path),
        "no_subdir": True,
        "rse": OFFSITE_RSE_2,
    }
    download_client = DownloadClient()
    download_client.download_dids([download_spec])

    # Verify the downloaded file content
    download_path = tmp_path / lfn.lstrip("/")
    msg = f"Download failed at {download_path}"
    assert download_path.is_file(), msg

    downloaded_content = download_path.read_text()
    msg = (
        f"Downloaded file content does not match the original. "
        f"Expected: {test_file_content}, Got: {downloaded_content}"
    )
    assert downloaded_content == test_file_content, msg


@pytest.mark.usefixtures("_auth_proxy")
@pytest.mark.verifies_usecase("UC-110-1.6")
def test_add_offsite_replication_rules_single_copy(
    pre_existing_lfn: str,
    test_scope: str,
    test_vo: str,
    storage_mount_path: Path,
    tmp_path: Path,
    onsite_test_file: tuple[Path, str],
    caplog,
):
    """Test the add_offsite_replication_rules method of IngestionClient with a single copy (copies=1)."""

    ingestion_client = IngestionClient(
        data_path=storage_mount_path,
        rse=ONSITE_RSE,
        vo=test_vo,
        scope=test_scope,
    )

    # Replicate the ACADA file to one offsite RSE
    lfn = pre_existing_lfn
    did = {"scope": test_scope, "name": lfn}

    _, test_file_content = onsite_test_file

    offsite_rse_expression = "OFFSITE"
    copies = 1
    rule_ids = ingestion_client.add_offsite_replication_rules(
        lfn=lfn,
        offsite_rse_expression=offsite_rse_expression,
        copies=copies,
        lifetime=None,
    )

    # Verify that only one rule was created
    msg = f"Expected exactly 1 rule ID, got {len(rule_ids)}: {rule_ids}"
    assert len(rule_ids) == 1, msg

    rule_id_offsite_1 = rule_ids[0]
    rule_client = RuleClient()

    # Wait for the offsite rule to complete
    wait_for_replication_status(rule_client, rule_id_offsite_1, expected_status="OK")

    # Verify the replica exists on exactly one of the offsite RSEs (either OFFSITE_RSE_1 or OFFSITE_RSE_2)
    replica_client = ReplicaClient()
    replicas = next(replica_client.list_replicas(dids=[did]))
    states = replicas.get("states", {})
    LOGGER.info(
        "Replica states for DID %s in test_add_offsite_replication_rules_single_copy: %s",
        did,
        states,
    )
    # Check that the replica exists on exactly one offsite RSE
    offsite_replica_count = sum(
        1 for rse in [OFFSITE_RSE_1, OFFSITE_RSE_2] if states.get(rse) == "AVAILABLE"
    )
    msg = f"Expected exactly 1 offsite replica (on either {OFFSITE_RSE_1} or {OFFSITE_RSE_2}), got {offsite_replica_count}: {states}"
    assert offsite_replica_count == 1, msg

    # Determine which offsite RSE the replica was created on
    target_offsite_rse = (
        OFFSITE_RSE_1 if states.get(OFFSITE_RSE_1) == "AVAILABLE" else OFFSITE_RSE_2
    )

    # Download the file from the target offsite RSE to verify its content
    download_spec = {
        "did": f"{test_scope}:{lfn}",
        "base_dir": str(tmp_path),
        "no_subdir": True,
        "rse": target_offsite_rse,
    }
    download_client = DownloadClient()
    download_client.download_dids([download_spec])

    # Verify the downloaded file content
    download_path = tmp_path / lfn.lstrip("/")
    msg = f"Download failed at {download_path}"
    assert download_path.is_file(), msg
    downloaded_content = download_path.read_text()
    msg = (
        f"Downloaded file content does not match the original. "
        f"Expected: {test_file_content}, Got: {downloaded_content}"
    )
    assert downloaded_content == test_file_content, msg


def test_verify_fits_file(tel_events_test_file):
    from bdms.acada_ingestion import verify_fits_checksum

    with fits.open(tel_events_test_file) as hdul:
        verify_fits_checksum(hdul)


@pytest.fixture
def broken_checksum(tmp_path):
    # create a fits file with a broken checksum
    path = tmp_path / "invalid.fits"

    table = Table({"foo": [1, 2, 3], "bar": [4.0, 5.0, 6.0]})
    hdul = fits.HDUList([fits.PrimaryHDU(), fits.BinTableHDU(table)])
    hdul.writeto(path, checksum=True)

    # break it
    with path.open("rb+") as f:
        # FITS files are stored in blocks of 2880 bytes
        # first chunk should be the primary header
        # second chunk the header of the bintable
        # third chunk the payload of the bintable
        # we write garbage somewhere into the payload of the table
        f.seek(2 * 2880 + 10)
        f.write(b"\x12\x34\xff")
    return path


def test_verify_fits_file_invalid_checksum(broken_checksum):
    from bdms.acada_ingestion import FITSVerificationError, verify_fits_checksum

    with fits.open(broken_checksum) as hdul:
        with pytest.raises(FITSVerificationError, match="CHECKSUM verification failed"):
            verify_fits_checksum(hdul)


def test_ingest_init(storage_mount_path):
    """Test that Ingest initializes correctly with given parameters."""
    ingestion_client = IngestionClient(
        data_path=storage_mount_path,
        rse=ONSITE_RSE,
        vo="ctao",
        scope="acada",
    )

    ingest = Ingest(
        client=ingestion_client,
        top_dir=storage_mount_path,
        num_workers=3,
        lock_file_path=storage_mount_path / "lockfile.lock",
        polling_interval=0.5,
        check_interval=0.2,
    )
    assert ingest.client == ingestion_client
    assert ingest.top_dir == storage_mount_path
    assert ingest.num_workers == 3
    assert ingest.lock_file_path == storage_mount_path / "lockfile.lock"
    assert ingest.polling_interval == 0.5
    assert ingest.check_interval == 0.2
    assert not ingest.stop_event.is_set()  # check stop_event initial state
    assert hasattr(ingest, "result_queue")
    assert hasattr(ingest, "task_counter")
    assert hasattr(ingest, "submitted_tasks")
    assert ingest.task_counter == 0
    assert len(ingest.submitted_tasks) == 0


def test_check_directory_valid(storage_mount_path, tmp_path, caplog):
    """Test _check_directory with a valid, readable directory."""
    ingestion_client = IngestionClient(
        data_path=storage_mount_path,
        rse=ONSITE_RSE,
        vo="ctao",
        scope="acada",
    )

    ingest = Ingest(
        client=ingestion_client,
        top_dir=tmp_path,
        num_workers=1,
        lock_file_path=storage_mount_path / "bdms_ingest.lock",
        polling_interval=0.5,
        check_interval=0.5,
    )
    ingest._check_directory()


def test_check_directory_invalid(storage_mount_path, tmp_path, caplog):
    """Test _check_directory with an invalid directory."""
    ingestion_client = IngestionClient(
        data_path=storage_mount_path,
        rse=ONSITE_RSE,
        vo="ctao",
        scope="acada",
        logger=LOGGER,
    )

    invalid_dir = tmp_path / "nonexistent"

    ingest = Ingest(
        client=ingestion_client,
        top_dir=invalid_dir,
        num_workers=1,
        lock_file_path=storage_mount_path / "bdms_ingest.lock",
        polling_interval=0.5,
        check_interval=0.5,
    )

    with pytest.raises(RuntimeError, match=f"Cannot read directory {invalid_dir}"):
        ingest._check_directory()
    assert f"Cannot read directory {invalid_dir}" in caplog.text


@pytest.mark.usefixtures("_auth_proxy")
def test_process_file_success(
    storage_mount_path, caplog, onsite_test_file, test_vo, test_scope
):
    """Test for checking successful ingestion with trigger file clean-up, depends on IngestionClient"""
    ingestion_client = IngestionClient(
        data_path=storage_mount_path,
        rse=ONSITE_RSE,
        vo=test_vo,
        scope=test_scope,
    )

    acada_path, test_file_content = onsite_test_file
    test_file = acada_path
    trigger_file = Path(str(test_file) + TRIGGER_SUFFIX)
    trigger_file.symlink_to(test_file)
    result = process_file(ingestion_client, str(test_file))

    assert result.file_size == len(test_file_content)
    assert not result.skipped
    assert not trigger_file.exists()
    assert "Successfully registered the replica for lfn" in caplog.text
    assert "Created 2 offsite replication rule(s) for LFN" in caplog.text


@pytest.mark.usefixtures("_auth_proxy")
def test_process_file_skipped(
    storage_mount_path, caplog, onsite_test_file, test_vo, test_scope
):
    """Test for checking skipped ingestion when replica already exists"""
    ingestion_client = IngestionClient(
        data_path=storage_mount_path,
        rse=ONSITE_RSE,
        vo=test_vo,
        scope=test_scope,
    )

    acada_path, test_file_content = onsite_test_file
    test_file = acada_path
    trigger_file = Path(str(test_file) + TRIGGER_SUFFIX)
    trigger_file.symlink_to(test_file)

    # process file for the first time
    result = process_file(ingestion_client, str(test_file))
    assert not result.skipped
    assert result.file_size == len(test_file_content)

    caplog.clear()
    # process file second time to verify it is skipped
    result = process_file(ingestion_client, str(test_file))
    assert result.skipped
    assert result.file_size == 0
    assert "Replica already exists" in caplog.text


@pytest.mark.usefixtures("_auth_proxy")
def test_process_file_failure(storage_mount_path, tmp_path):
    """Test for checking failure for invalid file paths"""
    ingestion_client = IngestionClient(
        data_path=storage_mount_path,
        rse=ONSITE_RSE,
        vo="ctao",
        scope="acada",
    )

    invalid_file = tmp_path / "invalid_file.fits"
    invalid_file.write_text("dummy content")
    trigger_file = Path(str(invalid_file) + TRIGGER_SUFFIX)
    trigger_file.symlink_to(invalid_file)

    # The file path is outside the data_path causing a ValueError in acada_to_lfn
    with pytest.raises(ValueError, match="is not within data_path"):
        process_file(ingestion_client, str(invalid_file))

    # Trigger file should still exist since ingestion failed
    msg = "Trigger file should not be removed when ingestion fails"
    assert trigger_file.is_symlink(), msg
    trigger_file.unlink()


def test_sequential_exclusion_lock_prevention(storage_mount_path, tmp_path):
    """Test that a second daemon instance cannot start when first is already running.

    This test validates sequential exclusion: when one ingestion daemon is already
    running and has acquired the lock, any subsequent attempt to start another
    daemon instance should fail with a clear error message.
    """
    lock_file = tmp_path / "sequential_test.pid"

    ingestion_client = IngestionClient(
        data_path=storage_mount_path,
        rse=ONSITE_RSE,
        vo="ctao",
        scope="acada",
    )

    # Create two identical instances
    kwargs = dict(
        client=ingestion_client,
        top_dir=tmp_path,
        lock_file_path=lock_file,
        num_workers=1,
        polling_interval=30.0,  # to avoid lots of logs for scanning
        check_interval=0.1,
    )
    ingest1 = Ingest(**kwargs)
    ingest2 = Ingest(**kwargs)

    try:
        # start first instance
        ingest1.run(block=False)

        # Verify first instance has acquired lock with content validation
        msg = "First instance should have created PID file"
        assert lock_file.exists(), msg

        # Verify the lock file contains current process PID or a valid PID
        current_pid = os.getpid()
        stored_pid = int(lock_file.read_text().strip())

        # The stored PID should be current process since we're running in same process
        msg = f"Expected PID {current_pid}, got {stored_pid}"
        assert stored_pid == current_pid, msg

        # Starting a second instance should error acquiring the lock
        with pytest.raises(
            RuntimeError, match="Another ingestion process is already running"
        ):
            ingest2.run(block=False)

    finally:
        ingest1.shutdown()

    assert not lock_file.exists(), msg


def test_concurrent_exclusion_lock_prevention(storage_mount_path, tmp_path):
    """Test FileLock behavior under true concurrent access - simultaneous daemon startup attempts.

    This test validates real concurrent scenario where multiple daemon instances
    attempt to acquire the same lock simultaneously, simulating race conditions
    that occur in production environments.
    """
    lock_file = tmp_path / "concurrent_test.pid"

    ingestion_client = IngestionClient(
        data_path=storage_mount_path,
        rse=ONSITE_RSE,
        vo="ctao",
        scope="acada",
    )

    # Create two identical instances
    kwargs = dict(
        client=ingestion_client,
        top_dir=tmp_path,
        lock_file_path=lock_file,
        num_workers=1,
        polling_interval=30.0,  # to avoid lots of logs for scanning
        check_interval=0.1,
    )
    ingest1 = Ingest(**kwargs)
    ingest2 = Ingest(**kwargs)
    results = {}

    # Synchronization barrier - both threads wait here until released
    start_barrier = threading.Barrier(3)  # 2 worker threads + 1 main thread

    def run_instance(instance_id, instance):
        """Run instance - both will try to start simultaneously."""
        try:
            # synchronize with other threads
            start_barrier.wait()

            instance.run(block=False)
            results[instance_id] = "success"
        except RuntimeError as e:
            if "Another ingestion process is already running" in str(e):
                results[instance_id] = f"lock_conflict: {str(e)}"
            else:
                results[instance_id] = f"unexpected_error: {str(e)}"
        except Exception as e:
            results[instance_id] = f"error: {str(e)}"

    # Create both threads
    thread1 = threading.Thread(
        target=run_instance, args=("first", ingest1), daemon=False
    )
    thread2 = threading.Thread(
        target=run_instance, args=("second", ingest2), daemon=False
    )

    # Start both threads - they will wait at the barrier
    thread1.start()
    thread2.start()

    # Release the barrier - both threads start simultaneously
    start_barrier.wait()

    # Wait for both to complete the lock acquisition attempt
    thread1.join(timeout=15)
    thread2.join(timeout=15)

    LOGGER.debug("True Concurrency tests: %s", results)

    # Shutdown both. Shutdown works even when not started.
    for ingest in (ingest1, ingest2):
        ingest.shutdown()

    # Verify results - Exactly ONE should succeed, ONE should fail
    msg = f"Both instances should complete, got: {results}"
    assert len(results) == 2, msg

    success_count = sum(1 for result in results.values() if result == "success")
    conflict_count = sum(1 for result in results.values() if "lock_conflict" in result)

    msg = f"Exactly ONE instance should succeed, got {success_count}: {results}"
    assert success_count == 1, msg

    msg = f"Exactly ONE instance should get lock conflict, got {conflict_count}: {results}"
    assert conflict_count == 1, msg

    # Verify the lock conflict has correct error message
    conflict_result = [r for r in results.values() if "lock_conflict" in r][0]
    msg = "Expected 'Another ingestion process is already running' message in conflict result"
    assert "Another ingestion process is already running" in conflict_result, msg

    msg = "Lock file should be cleaned up"
    assert not lock_file.exists(), msg


def acada_write_test_files(
    storage_mount_path, test_vo, test_scope, n_files=7
) -> list[Path]:
    """Represents ACADA writing test files to the storage mount path."""
    timestamp = f"{datetime.now(timezone.utc):%Y-%m-%dT%H-%M-%S}"
    prefix = secrets.token_hex(4)

    test_subdir = f"data_{timestamp}_{prefix}"
    test_dir = storage_mount_path / test_vo / test_scope / test_subdir
    test_dir.mkdir(parents=True, exist_ok=True)

    # Create n_files dummy FITS files
    data_files = []
    rng = np.random.default_rng()
    for i in range(n_files):
        data_file = test_dir / f"testfile_{i}.fits"
        hdu = fits.PrimaryHDU(rng.random((50, 50)))
        hdu.writeto(data_file, overwrite=True, checksum=True)
        data_files.append(data_file)

        LOGGER.info("Created test file: %s", data_file)

    # Move permission reset before daemon start to avoid timing issues
    reset_xrootd_permissions(storage_mount_path)
    return data_files


def acada_create_trigger_symlink(data_file):
    """Represents creating a trigger symlink for a given data file."""

    try:
        trigger_file = Path(str(data_file) + TRIGGER_SUFFIX)
        trigger_file.symlink_to(data_file)
        LOGGER.info("Created trigger file: %s -> %s", trigger_file, data_file)
        return trigger_file

    except Exception as e:
        raise RuntimeError(f"Failed to create trigger for {data_file}: {e}") from e


def create_unique_test_dir(storage_mount_path, test_vo, test_scope):
    """Create a unique test directory."""
    return storage_mount_path / test_vo / test_scope / f"test_{uuid.uuid4().hex[:8]}"


@pytest.fixture
def create_test_file_with_trigger():
    """Create a test FITS file and its trigger file and also cleanup."""

    data_file = None
    trigger_file = None

    def _create_files(test_dir, filename="test_file.fits"):
        nonlocal data_file, trigger_file
        data_file = test_dir / filename
        hdu = fits.PrimaryHDU(RNG.random((10, 10)))
        hdu.writeto(data_file, overwrite=True, checksum=True)

        trigger_file = Path(str(data_file) + TRIGGER_SUFFIX)
        trigger_file.symlink_to(data_file)

        return data_file, trigger_file

    yield _create_files

    if trigger_file is not None and trigger_file.is_symlink():
        trigger_file.unlink()


@pytest.fixture
def setup_test_files_with_triggers(storage_mount_path, test_vo, persistent_test_scope):
    """Create test files with triggers using persistent scope and clean up after test."""
    data_files = []
    trigger_files = []
    expected_lfns = []

    try:
        data_files = acada_write_test_files(
            storage_mount_path, test_vo, persistent_test_scope
        )

        for data_file in data_files:
            trigger_file = acada_create_trigger_symlink(data_file)
            trigger_files.append(trigger_file)
            expected_lfns.append(f"/{data_file.relative_to(storage_mount_path)}")

        yield data_files, trigger_files, expected_lfns

    finally:
        # Clean up
        for trigger_file in trigger_files:
            if trigger_file.is_symlink():
                trigger_file.unlink()


@pytest.fixture
def ingest_daemon_test(storage_mount_path, test_vo, test_scope, tmp_path):
    """Create and manage ingest daemon for tests."""
    test_data_dir = create_unique_test_dir(storage_mount_path, test_vo, test_scope)
    test_data_dir.mkdir(parents=True, exist_ok=True)

    ingest = setup_ingest(
        storage_mount_path, test_vo, test_scope, test_data_dir, tmp_path
    )

    yield ingest, test_data_dir

    ingest.shutdown()


@pytest.mark.usefixtures(
    "_auth_proxy", "lock_for_ingestion_daemon", "disable_ingestion_daemon"
)
@pytest.mark.verifies_usecase("UC-110-1.1.4")
def test_ingest_parallel_submission(storage_mount_path, caplog, test_vo, test_scope):
    """Test parallel file processing: creates multiple FITS files simultaneously and verifies that the
    daemon can detect, process, and ingest them efficiently using parallel workers.
    """
    ingestion_client = IngestionClient(
        data_path=storage_mount_path,
        rse=ONSITE_RSE,
        vo=test_vo,
        scope=test_scope,
    )

    ingest = Ingest(
        client=ingestion_client,
        top_dir=storage_mount_path,
        num_workers=4,
        lock_file_path=storage_mount_path / "bdms_ingest.lock",
        polling_interval=0.5,
        check_interval=0.5,
    )

    data_files = acada_write_test_files(storage_mount_path, test_vo, test_scope)
    n_data_files = len(data_files)

    try:
        ingest.run(block=False)

        # Create trigger files and also track
        trigger_files = []

        for data_file in data_files:
            trigger_file = data_file.with_name(data_file.name + TRIGGER_SUFFIX)
            trigger_file.symlink_to(data_file.relative_to(data_file.parent))
            trigger_files.append(trigger_file)

        # Wait for processing with concurrency monitoring
        processing_timeout = 120.0
        processing_start = time.perf_counter()
        processed_files = 0

        while time.perf_counter() - processing_start < processing_timeout:
            # Check processing completion
            processed_files = sum(
                1
                for df in data_files
                if f"Processed file {df} with result" in caplog.text
            )

            # an error occurred
            if "Fatal error in result processing thread" in caplog.text:
                break

            # all done
            if processed_files == n_data_files:
                break

            time.sleep(0.5)

        duration = time.perf_counter() - processing_start
        error = f"Only {processed_files} of {n_data_files} files processed successfully in {duration}"
        assert processed_files == 7, error

        # Record ingestion workflow completion time
    finally:
        # Stop the daemon
        ingest.shutdown()

    # Verify results
    assert "Started process pool with 4 workers" in caplog.text
    assert "Result processing thread started" in caplog.text

    # Verify trigger files were cleaned up during successful processing
    remaining_triggers = sum(1 for tf in trigger_files if tf.exists())
    error = f"Expected all trigger files to be cleaned up, {remaining_triggers} remain"
    assert remaining_triggers == 0, error

    # Verify clean shutdown
    assert not ingest.lock_file_path.exists()
    assert "Stopped ingestion daemon" in caplog.text
    assert "Result processing thread stopped" in caplog.text

    # Test daemon restart with new file
    caplog.clear()

    # Create new file while ingestion daemon is not running
    new_data_file = storage_mount_path / test_vo / test_scope / "new_file.fits"
    new_data_file.parent.mkdir(parents=True, exist_ok=True)
    new_data_file.write_text("some dummy content")

    new_trigger_file = Path(str(new_data_file) + TRIGGER_SUFFIX)
    new_trigger_file.symlink_to(new_data_file)

    # Restart daemon
    try:
        ingest.run(block=False)

        # Wait for new file processing
        new_start = time.perf_counter()

        while time.perf_counter() - new_start < 30.0:
            if f"Processed file {new_data_file} with result" in caplog.text:
                break
            time.sleep(0.5)
        else:
            pytest.fail("New file was not processed after restart")

        new_file_processing_time = time.perf_counter() - new_start
        assert not new_trigger_file.exists(), "New trigger file was not cleaned up"
    finally:
        shutdown_start = time.perf_counter()
        ingest.shutdown()
        ingest_end = time.perf_counter()
        shutdown_duration = ingest_end - shutdown_start

    error = "Re-started daemon did not terminate within timeout of 10 s"
    assert shutdown_duration < 10, error

    # Statistics
    detection_to_completion_time = ingest_end - processing_start
    processing_rate = (
        processed_files / detection_to_completion_time
        if detection_to_completion_time > 0
        else 0
    )

    total_submitted = ingest.task_counter
    tasks_cleaned_up = len(ingest.submitted_tasks) == 0

    LOGGER.info("=== Parallel Ingestion Test Results ===")
    LOGGER.info(
        "Files processed: %d/7 in %.1fs",
        processed_files,
        detection_to_completion_time,
    )
    LOGGER.info("Processing rate: %.1f files/sec", processing_rate)
    LOGGER.info("Total tasks submitted: %d", total_submitted)
    LOGGER.info("Task cleanup successful: %s", tasks_cleaned_up)
    LOGGER.info("New file after restart: processed in %.1fs", new_file_processing_time)


def fetch_ingestion_daemon_metrics():
    """Fetch metrics from the ingestion daemon to verify its operation."""

    response = urlopen("http://bdms-ingestion-daemon:8000/")

    msg = "Ingestion daemon metrics are not responding"
    assert response.status == 200, msg

    n_tasks_metrics = {}
    for line in response.readlines():
        line = line.decode("utf-8").strip()
        if line.startswith("n_tasks_"):
            LOGGER.info("Ingestion daemon metrics: %s", line)
            key, value = line.split(" ", 1)
            n_tasks_metrics[key] = float(value)

    return n_tasks_metrics


@pytest.mark.usefixtures("_auth_proxy")
def test_scan_for_triggers_success(
    caplog, ingest_daemon_test, create_test_file_with_trigger
):
    """Test _scan_for_triggers detects new trigger files and tracks them."""

    ingest, test_data_dir = ingest_daemon_test
    data_file, trigger_file = create_test_file_with_trigger(test_data_dir)

    with caplog.at_level(logging.DEBUG, logger="bdms.acada_ingestion.Ingest"):
        try:
            ingest.run(block=False)
            time.sleep(1.0)  # Allow one scanning cycle
        finally:
            ingest.shutdown()

    assert "Scanned for triggers: found 1 total, 1 new" in caplog.text
    assert (
        f"Processing trigger file {trigger_file}, submitting data file {data_file}"
        in caplog.text
    )
    assert "Submitting task 0 for file" in caplog.text
    assert not trigger_file.exists()


@pytest.mark.usefixtures("_auth_proxy")
def test_scan_for_triggers_no_new_triggers(
    caplog, ingest_daemon_test, create_test_file_with_trigger
):
    """Test that daemon does not resubmit already known triggers."""
    ingest, test_data_dir = ingest_daemon_test

    with caplog.at_level(logging.DEBUG, logger="bdms.acada_ingestion.Ingest"):
        _, trigger_file = create_test_file_with_trigger(test_data_dir)
        # Add trigger to known_triggers to simulate it was already processed
        ingest.known_triggers.add(trigger_file)

        try:
            # perform scan manually
            ingest._scan_for_triggers()

            assert "Scanned for triggers: found 1 total, 0 new" in caplog.text
            msg = "No trigger files should be processed"
            assert "Processing trigger file" not in caplog.text, msg
            assert len(ingest.submitted_tasks) == 0
            assert len(ingest.known_triggers) == 1
        finally:
            trigger_file.unlink()


class MockExecutor:
    def __init__(self):
        self.tasks = []

    def submit(self, func, *args, **kwargs):
        self.tasks.append((func, args, kwargs))
        return Future()


class MockQueue(list):
    def submit(self, path):
        self.append(path)


@pytest.mark.usefixtures("_auth_proxy")
def test_process_trigger_file_success(
    storage_mount_path,
    test_vo,
    test_scope,
    caplog,
    tmp_path,
    create_test_file_with_trigger,
):
    """Test _process_trigger_file successfully submits a valid data file."""
    test_data_dir = create_unique_test_dir(storage_mount_path, test_vo, test_scope)

    ingest = setup_ingest(
        storage_mount_path, test_vo, test_scope, test_data_dir, tmp_path
    )

    test_data_dir.mkdir(parents=True, exist_ok=True)
    data_file, trigger_file = create_test_file_with_trigger(test_data_dir)

    ingest.executor = MockExecutor()

    with caplog.at_level(logging.DEBUG, logger="bdms.acada_ingestion.Ingest"):
        ingest._process_trigger_file(trigger_file)

    # Verify trigger file processed and the task was submitted
    assert (
        f"Processing trigger file {trigger_file}, submitting data file {data_file}"
        in caplog.text
    )
    assert f"Submitting task 0 for file {data_file}" in caplog.text
    assert f"Successfully processed trigger {trigger_file}" in caplog.text

    msg = "Task counter not incremented"
    assert ingest.task_counter == 1, msg


@pytest.mark.usefixtures("_auth_proxy")
def test_polling_loop_success(
    storage_mount_path,
    test_vo,
    test_scope,
    caplog,
    tmp_path,
    create_test_file_with_trigger,
):
    """Test _polling_loop runs and processes trigger files until stopped."""
    test_data_dir = (
        storage_mount_path / test_vo / test_scope / f"test_{uuid.uuid4().hex[:8]}"
    )
    test_data_dir.mkdir(parents=True, exist_ok=True)

    ingest = setup_ingest(
        storage_mount_path, test_vo, test_scope, test_data_dir, tmp_path
    )

    data_file, trigger_file = create_test_file_with_trigger(test_data_dir)

    # mock submitting files so we do not actually do anything
    submitted_files = MockQueue()
    ingest._submit_file = submitted_files.submit

    with caplog.at_level(logging.DEBUG, logger="bdms.acada_ingestion.Ingest"):
        try:
            ingest.run(block=False)
            time.sleep(1.5)
        finally:
            ingest.shutdown()

    assert submitted_files == [str(data_file)]
    assert (
        f"Starting polling of directory {test_data_dir} every 0.5 seconds"
        in caplog.text
    )
    assert (
        f"Processing trigger file {trigger_file}, submitting data file {data_file}"
        in caplog.text
    )
    assert "Stopped polling for new trigger files" in caplog.text


@pytest.mark.usefixtures(
    "_auth_proxy", "lock_for_ingestion_daemon", "enable_ingestion_daemon"
)
@pytest.mark.verifies_usecase("UC-110-1.1.4")
def test_ingest_parallel_submission_with_live_daemon(setup_test_files_with_triggers):
    """Test parallel file processing with an already running daemon."""
    metrics_before_test = fetch_ingestion_daemon_metrics()
    # metrics should be 0 as we restart the daemon
    for k in ("success", "processed", "skipped"):
        assert metrics_before_test[f"n_tasks_{k}_total"] == 0

    data_files, trigger_files, expected_lfns = setup_test_files_with_triggers

    try:
        wait_for_trigger_file_removal(trigger_files, timeout=120.0)
        wait_for_replicas(expected_lfns)

        # make sure that metrics are available from the daemon
        metrics = fetch_ingestion_daemon_metrics()

        def difference(key):
            return metrics[key] - metrics_before_test[key]

        assert metrics["n_tasks_success_created"] < time.time()
        assert difference("n_tasks_processed_total") == len(data_files)

        n_skipped_or_success = (
            metrics["n_tasks_success_total"] + metrics["n_tasks_skipped_total"]
        )
        error = "Ingestion daemon metrics do not match expected values"
        assert difference("n_tasks_processed_total") == n_skipped_or_success, error

    finally:
        deployment_scale("ingestion-daemon", 0)


@pytest.mark.usefixtures(
    "_auth_proxy", "lock_for_ingestion_daemon", "disable_ingestion_daemon"
)
def test_ingest_detects_existing_files_with_live_daemon(
    storage_mount_path, test_vo, setup_test_files_with_triggers
):
    """Test for ingestion daemon detecting and processing already existing files created before it started running."""

    test_scope = "test_scope_persistent"

    data_files, trigger_files, expected_lfns = setup_test_files_with_triggers

    LOGGER.info(
        "Created %d files and triggers while daemon is not running", len(data_files)
    )

    # Verify trigger files exist before starting daemon
    existing_triggers = list(
        (storage_mount_path / test_vo / test_scope).glob("*.trigger")
    )
    if existing_triggers:
        LOGGER.info("Trigger files created: %d", len(existing_triggers))
        for tf in existing_triggers:
            LOGGER.info("Created: %s", tf)

    try:
        # Start the ingestion daemon pod once files are created
        deployment_scale("ingestion-daemon", 1)

        wait_for_trigger_file_removal(trigger_files, timeout=120.0)
        wait_for_replicas(expected_lfns)

        LOGGER.info(
            "Ingestion daemon successfully detected and processed existing files"
        )

        # make sure that metrics are available from the daemon
        n_tasks_metrics = fetch_ingestion_daemon_metrics()

        files_processed = n_tasks_metrics["n_tasks_processed_total"]
        files_success = n_tasks_metrics["n_tasks_success_total"]
        files_skipped = n_tasks_metrics["n_tasks_skipped_total"]
        msg = f"Expected {len(data_files)} files processed, got {files_processed}"
        assert files_processed == len(data_files), msg

        LOGGER.info(
            "Ingestion daemon metrics verified: processed %d files (%d success, %d skipped)",
            files_processed,
            files_success,
            files_skipped,
        )

    finally:
        # Stop daemon: shutdown
        deployment_scale("ingestion-daemon", 0)


@pytest.mark.parametrize(
    "expected_message",
    [
        "empty data file name",
        "data path {data_path} missing",
        "data path {data_path} is not a file",
    ],
)
def test_invalid_trigger_files(
    expected_message,
    storage_mount_path,
    test_vo,
    test_scope,
    caplog,
    tmp_path,
):
    """
    Regression test for bug #131, ingestion of a trigger link just named .trigger

    In case of a file just called ".trigger" pointing to an existing file
    in the link itself was ingested. While this should never happen in production,
    this is a clear bug.
    """

    test_data_dir = (
        storage_mount_path / test_vo / test_scope / f"test_{uuid.uuid4().hex[:8]}"
    )
    test_data_dir.mkdir(parents=True, exist_ok=True)

    ingest = setup_ingest(
        storage_mount_path,
        test_vo,
        test_scope,
        top_dir=test_data_dir,
        lock_base_path=tmp_path,
    )

    # mock submitting files, we only want to check the behavior of the submission logic
    submitted_files = MockQueue()
    ingest._submit_file = submitted_files.submit

    # create dummy data path / trigger file for expected_message
    if "empty" in expected_message:
        data_path = test_data_dir / "test.dat"
        data_path.write_text("test")
        trigger_file = test_data_dir / ".trigger"
    elif "missing" in expected_message:
        data_path = test_data_dir / "test.dat"
        trigger_file = data_path.with_name(data_path.name + TRIGGER_SUFFIX)
    else:
        data_path = test_data_dir / "subdir"
        data_path.mkdir()
        trigger_file = data_path.with_name(data_path.name + TRIGGER_SUFFIX)

    trigger_file.symlink_to(data_path.relative_to(test_data_dir))

    try:
        with caplog.at_level(logging.ERROR, logger="bdms.acada_ingestion.Ingest"):
            caplog.clear()
            # scan for files once, manually.
            ingest._scan_for_triggers()

        assert len(submitted_files) == 0
        assert len(caplog.records) == 1
        assert caplog.records[0].levelname == "ERROR"

        trigger_part = f"Ignoring trigger file: {trigger_file}, "
        data_part = expected_message.format(data_path=data_path)
        assert caplog.records[0].message == trigger_part + data_part
    finally:
        trigger_file.unlink()
        if data_path.is_dir():
            data_path.rmdir()
        elif data_path.is_file():
            data_path.unlink()
