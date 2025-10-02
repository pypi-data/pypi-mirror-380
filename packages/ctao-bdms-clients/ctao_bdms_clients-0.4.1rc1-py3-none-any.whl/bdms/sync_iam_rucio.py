"""Sync IAM users and identities into Rucio accounts."""

import logging
import os
import time
from configparser import ConfigParser
from typing import Optional

import requests
from rucio.client.accountclient import AccountClient
from rucio.common.exception import AccountNotFound, RucioException

logging.basicConfig(level=logging.INFO)

CONFIG_ENV_VAR = "BDMS_SYNC_CONFIG"


def load_config(config_path):
    """Load configuration from file and environment variables."""
    cfg = ConfigParser()
    read = cfg.read(config_path)

    if len(read) != 1:
        raise ValueError(f"Failed to read config file {config_path}")

    if not cfg.has_section("IAM"):
        raise ValueError("Config is missing IAM section")

    section = cfg["IAM"]
    return dict(
        iam_server=section["iam-server"],
        client_id=section["client-id"],
        client_secret=section["client-secret"],
        max_retries=section.getint("max-retries", fallback=5),
        retry_delay=section.getfloat("delay", fallback=10.0),
    )


class IAMRucioSync:
    """Synchronize IAM accounts, identities into Rucio."""

    TOKEN_URL = "/token"

    def __init__(
        self,
        *,
        iam_server: str,
        client_id: str,
        client_secret: str,
        max_retries: int = 5,
        retry_delay: float = 10.0,
    ):
        """Initialize the syncer and load configuration."""
        self.iam_server = iam_server
        self.client_id = client_id
        self.client_secret = client_secret
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.account_client = AccountClient()

    def get_token(self) -> str:
        """Obtain an access token from the IAM server."""
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
            "scope": "scim:read",
        }
        logging.info(
            "Requesting IAM token from %s using the client_id %s",
            self.iam_server + self.TOKEN_URL,
            self.client_id,
        )
        for attempt in range(1, self.max_retries + 1):
            try:
                r = requests.post(
                    self.iam_server + self.TOKEN_URL,
                    data=data,
                    timeout=30,
                )
                r.raise_for_status()  # exception is status!=200
                js = r.json()
                if "access_token" not in js:
                    raise RuntimeError(f"No access_token in response: {js}")
                return js["access_token"]

            except (requests.RequestException, RuntimeError) as e:
                if attempt < self.max_retries:
                    logging.error(
                        "attempt %d failed: %s. Retrying in %d seconds...",
                        attempt,
                        e,
                        self.retry_delay,
                    )
                    time.sleep(attempt * self.retry_delay)
                else:
                    raise

    def get_users(self, token: str) -> list[dict]:
        """Fetch users from IAM using SCIM API."""
        start = 1
        count = 100
        headers = {"Authorization": f"Bearer {token}"}
        users = []
        processed = 0
        while True:
            params = {"startIndex": start, "count": count}
            r = requests.get(
                f"{self.iam_server}/scim/Users",
                headers=headers,
                params=params,
                timeout=30,
            )
            data = r.json()
            users.extend(data.get("Resources", []))
            processed += data.get("itemsPerPage", 0)
            if processed < data.get("totalResults", 0):
                start += count
            else:
                break
        logging.info("Fetched %d IAM users", len(users))
        return users

    def ensure_group_account(self, account_name: str) -> bool:
        """Ensure a Rucio account exists for the given user."""
        try:
            self.account_client.get_account(account_name)
            return False
        except AccountNotFound:
            self.account_client.add_account(account_name, "GROUP", email="")
            return True

    def existing_identities(self, account: str) -> set[str]:
        """Return the existing identities for a given account."""
        try:
            return {i["identity"] for i in self.account_client.list_identities(account)}
        except RucioException as e:
            logging.error("List identities failed %s: %s", account, e)
            return set()

    def sync_users(self, users: list[dict]) -> None:
        """Create Rucio accounts and identities for given IAM users."""
        for user in users:
            try:
                self.sync_user(user)
            except Exception:
                logging.exception("Error syncing user: %s", user)

    def sync_user(self, user: dict) -> None:
        """Create account and identities for a given IAM user."""
        email = self._get_user_email(user)

        logging.info("Syncing groups for user %s", email)
        for group in user.get("groups", []):
            groupname = group["display"]
            account_name = self.iam_to_rucio_groupname(groupname)

            self.ensure_group_account(account_name)
            certificates = self._get_user_certificates(user)
            self._sync_group_certificates(account_name, email, certificates)

    def _get_user_email(self, user: dict) -> str:
        return user.get("emails", [{}])[0].get("value", "")

    def _get_user_certificates(self, user: dict) -> list[dict]:
        indigo = user.get("urn:indigo-dc:scim:schemas:IndigoUser", {})
        return indigo.get("certificates", [])

    def _sync_group_certificates(
        self, groupname: str, email: str, certificates: list[dict]
    ) -> None:
        existing_identities = self.existing_identities(groupname)
        for cert in certificates:
            dn = self._extract_dn(cert)
            if not dn:
                continue
            if dn in existing_identities:
                logging.info("Identity %s already exists for group %s", dn, groupname)
                continue
            self._add_x509_identity(dn, groupname, email)

    def _extract_dn(self, cert: dict) -> Optional[str]:
        dn = cert.get("subjectDn")
        if not dn:
            logging.error("Missing subjectDn in %s", cert)
            return None
        return self.to_gridmap(dn)

    def _add_x509_identity(self, dn: str, account: str, email: str) -> None:
        try:
            self.account_client.add_identity(
                identity=dn,
                authtype="X509",
                account=account,
                email=email,
                default=True,
            )
            logging.info("Added X509 identity %s to account %s", dn, account)
        except Exception as e:
            logging.error("X509 add failed %s: %s", account, e)

    @staticmethod
    def to_gridmap(dn: str) -> str:
        """Convert a DN string into gridmap format."""
        parts = dn.split(",")
        parts.reverse()
        return "/".join(parts)

    @staticmethod
    def iam_to_rucio_groupname(groupname: str):
        """Convert iam group name to rucio account name, replacing invalid chars."""
        return groupname.replace(".", "_")


def main():
    """Entry point: run the IAM → Rucio synchronization."""
    config_path = os.environ.get(CONFIG_ENV_VAR)

    if not config_path:
        raise SystemExit("Config path required. Set %s.", CONFIG_ENV_VAR)
    if not os.path.isfile(config_path):
        raise SystemExit(f"Config file not found: {config_path}")

    config = load_config(config_path)
    syncer = IAMRucioSync(**config)
    token = syncer.get_token()
    users = syncer.get_users(token)
    syncer.sync_users(users)
    logging.info("Sync done.")


if __name__ == "__main__":
    main()
