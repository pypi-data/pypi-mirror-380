import json
import os
from datetime import datetime
from pathlib import Path

from gpas.constants import (
    DEFAULT_HOST,
    DEFAULT_PROTOCOL,
    DEFAULT_UPLOAD_HOST,
)
from gpas.log_utils import logger


def get_protocol() -> str:
    """Get the protocol to use for communication.

    Returns:
        str: The protocol (e.g., 'http', 'https').
    """
    if "GPAS_PROTOCOL" in os.environ:
        return os.environ["GPAS_PROTOCOL"]
    else:
        return DEFAULT_PROTOCOL


def get_host(cli_host: str | None = None) -> str:
    """Return hostname using 1) CLI argument, 2) environment variable, 3) default value.

    Args:
        cli_host (str | None): The host provided via CLI argument.

    Returns:
        str: The resolved hostname.
    """
    return (
        cli_host if cli_host is not None else os.environ.get("GPAS_HOST", DEFAULT_HOST)
    )


def get_upload_host(cli_host: str | None = None) -> str:
    """Return hostname using 1) CLI argument, 2) environment variable, 3) default value.

    Args:
        cli_host (str | None): The host provided via CLI argument.

    Returns:
        str: The resolved hostname.
    """
    return (
        cli_host
        if cli_host is not None
        else os.environ.get("GPAS_UPLOAD_HOST", DEFAULT_UPLOAD_HOST)
    )


def get_token_path(host: str) -> Path:
    """Get the path to the token file for a given host.

    Args:
        host (str): The host for which to get the token path.

    Returns:
        Path: The path to the token file.
    """
    conf_dir = Path.home() / ".config" / "gpas"
    token_dir = conf_dir / "tokens"
    token_dir.mkdir(parents=True, exist_ok=True)
    token_path = token_dir / f"{host}.json"
    return token_path


def get_token_expiry(host: str) -> datetime | None:
    """Get the expiry date of the token for a given host.

    Args:
        host (str): The host for which to get the token expiry date.

    Returns:
        datetime | None: The expiry date of the token, or None if the token does not exist.
    """
    token_path = get_token_path(host)
    if token_path.exists():
        try:
            with open(token_path) as token_string:
                token: dict = json.load(token_string)
                expiry = token.get("expiry", False)
                if expiry:
                    return datetime.fromisoformat(expiry)
        except json.JSONDecodeError:
            return None
    return None


def is_auth_token_live(host: str) -> bool:
    """Check if the authentication token for a given host is still valid.

    Args:
        host (str): The host for which to check the token validity.

    Returns:
        bool: True if the token is still valid, False otherwise.
    """
    expiry = get_token_expiry(host)
    if expiry:
        logger.debug(f"Token expires: {expiry}")
        return expiry > datetime.now()
    return False


def get_access_token(host: str) -> str:
    """Reads token from ~/.config/gpas/tokens/<host>.

    Args:
        host (str): The host for which to retrieve the token.

    Returns:
        str: The access token.
    """
    token_path = get_token_path(host)
    logger.debug(f"Getting token path: {token_path}")
    try:
        data = json.loads(token_path.read_text())
    except FileNotFoundError as fne:
        logger.exception("Can't find access token")
        raise FileNotFoundError(
            f"Token not found at {token_path}, have you authenticated?"
        ) from fne
    return data["access_token"].strip()
