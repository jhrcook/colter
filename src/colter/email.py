"""Email."""

from datetime import datetime

import yagmail

from . import secrets


def send_email() -> None:
    """Send notification email."""
    contents = [
        "Colter Thorofare Net is back in stock!",
        f"timestamp: {datetime.now()}",
    ]
    yag = yagmail.SMTP("appleid0023", secrets.get_password())
    yag.send("joshuacook0023@gmail.com", "Thorofare Net scraper", contents)
