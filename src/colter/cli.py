"""Command line interface."""

from time import sleep
from typing import Final

from loguru import logger
from typer import Typer

from . import email, scraper

app = Typer(add_completion=False)

MAX_ERRORS: Final[int] = 3
RETRY_RATE: Final[int] = 2 * 60 * 60  # Time in seconds to wait between requests.


@app.command()  # type: ignore
def main() -> None:
    error_count: int = 0
    while True:
        try:
            is_sold_out = scraper.is_thorofare_net_soldout()
        except BaseException as err:
            logger.error(f"An error occurred while scraping the product page: {err}.")
            error_count += 1
            continue

        if is_sold_out:
            logger.info("The Thorofare Net is still sold out.")
        else:
            logger.info("The Thorofare Net is back in stock!")
            logger.info("Sending email.")
            email.send_email()
            logger.info("Email sent, breaking loop.")
            break

        sleep(RETRY_RATE)
