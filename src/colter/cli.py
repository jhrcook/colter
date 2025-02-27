"""Command line interface."""

from typing import Final

from loguru import logger
from typer import Exit, Typer

from . import email, scraper

app = Typer(add_completion=False)

MAX_ERRORS: Final[int] = 3
RETRY_RATE: Final[int] = 120  # Time in minutes to wait between requests.


@app.command()  # type: ignore
def main() -> None:
    try:
        is_sold_out = scraper.is_thorofare_net_soldout()
    except BaseException as err:
        logger.error(f"An error occurred while scraping the product page: {err}.")
        Exit(1)

    if is_sold_out:
        logger.info("The Thorofare Net is still sold out.")
    else:
        logger.info("The Thorofare Net is back in stock!")
        logger.info("Sending email.")
        email.send_email()
        logger.info("Email sent, breaking loop.")

    Exit(0)
