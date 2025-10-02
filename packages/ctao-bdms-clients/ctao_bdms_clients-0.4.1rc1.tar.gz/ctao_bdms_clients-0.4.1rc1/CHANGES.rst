BDMS v0.4.0 (2025-09-24)
------------------------


Bug Fixes
~~~~~~~~~

- Add service account needed for bootstrap jobs to restart rucio rollout. [`!138 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/138>`__]

- Let acada ingest exit gracefully on SIGTERM. [`!148 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/148>`__]

- Change polling method enabling discovery of existing trigger files in ACADA ingestion [`!129 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/129>`__]

New Features
~~~~~~~~~~~~

- Add new helm chart values settings, allowing to customize rucio client:

  .. code-block:: yaml

     rucio_client_config:
       configMapName:
       createConfigMap: true [`!137 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/137>`__]

- Update Rucio to version 38 LTS. [`!143 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/143>`__]

- Add running Rucio database migrations to helm chart init job. [`!143 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/143>`__]

- Add DPPS IAM subchart for testing of source of identity management. [`!154 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/154>`__]

- Add a synchronization pod to export IAM groups and certificates into Rucio groups and identities [`!156 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/156>`__]


BDMS v0.3.1 (2025-07-24)
------------------------
Patch release with minor improvements and bugfixes

New Feature
~~~~~~~~~~~

- Add ingested file size prometheus metric to ingestion daemon. [`!134 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/134>`__]


Refactoring and Optimization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Reduce log-level of charset_normalizer channel from DEBUG to WARNING  [`!133 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/133>`__]
- Simplify error handling of ingest process for ACADA data Products [`!134 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/134>`__]


BDMS v0.3.0 (2025-06-27)
------------------------

New Features
~~~~~~~~~~~~

- Add BDMS Ingestion Daemon (UC-110-1.1.4) [`!111 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/111>`__]

Refactoring and Optimization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Make hooks optional, enabling faster startup. [`!113 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/113>`__]


BDMS v0.2.1 (2025-06-03)
------------------------

Bugfix release to allow (pre-)production deployment without test storages.

Bug Fixes
~~~~~~~~~

- Allow to further configure first test RSE: set storageclass and make optional. [`!112 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/112>`__]


BDMS 0.2.0 (2025-05-07)
-----------------------


API Changes
~~~~~~~~~~~

- Add basic ingestion of ACADA files (UC-110-1.1.1) [`!76 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/76>`__]

- Replicate Data Products (UC-110-1.6) with test case for copies=2 [`!83 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/83>`__]

- Extraction of metadata from ACADA-LST DL0 FITS files and adding metadata to ingested file (UC-110-1.1.1) [`!85 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/85>`__]

- Add test case for copies=1 for the replication (UC-110-1.6) [`!87 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/87>`__]


Bug Fixes
~~~~~~~~~

- Add missing permissions to fix onsite storage permissions [`!103 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/103>`__]


New Features
~~~~~~~~~~~~

- Adapt one RSE as onsite and exposing its diskspace to client test pod [`!69 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/69>`__]

- Add dcache and its dependencies in the BDMS helm chart (UC-170-1.6) [`!80 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/80>`__]

- Add FITS checksum verification [`!94 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/94>`__]

- Make storage configurable by providing additional config for RSE and also make xrootd image configurable [`!96 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/96>`__]


Maintenance
~~~~~~~~~~~

- Fix rucio server not using correct lfn2pfn algorithm [`!72 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/72>`__]

- Use test_vo fixture for ingestion tests [`!81 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/81>`__]

- Update dpps release for test report and signature matrix [`!82 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/82>`__]

- Update BDMS docs for Rel 0.1 [`!89 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/89>`__]

- Update fts image and toolkit [`!90 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/90>`__]

- Added download_test_file in utils.py to download a FITS file from MinIO server [`!93 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/93>`__]

- Update rucio to 35.7.0 [`!97 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/97>`__]

- Update FTS subchart version [`!99 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/99>`__]

- Resolve Test container build fails due to missing -y in autoremove [`!101 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/101>`__]


Refactoring and Optimization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Update FTS chart to 0.3 to reduce integration test time [`!100 <https://gitlab.cta-observatory.org/cta-computing/dpps/bdms/bdms/-/merge_requests/100>`__]

BDMS v0.1.0 (2025-02-21)
---------------------------

First release of the Bulk Data Management System (BDMS).

* Deployment of Rucio 35.4 using helm.
* Client package pinning the correct rucio and rucio policy package versions.
* Integration tests for DPPS release 0.0 use cases.
