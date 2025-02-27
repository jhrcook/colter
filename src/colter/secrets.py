"""Secrets."""


def get_password() -> str:
    """Get email password from secrets file."""
    with open(".secrets", "r") as file:
        return file.read().strip()
