"""Secrets."""

import os


def get_password() -> str:
    """Get email password from secrets file."""
    if (pswd := os.getenv("EMAIL_PASSWORD")) is not None:
        return pswd

    with open(".secrets", "r") as file:
        return file.read().strip()
