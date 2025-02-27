"""Command line interface."""

from time import sleep
from typing import Annotated, Final

from loguru import logger
from typer import Option, Typer

from . import email, scraper

app = Typer(add_completion=False)

MAX_ERRORS: Final[int] = 3
RETRY_RATE: Final[int] = 120  # Time in minutes to wait between requests.


@app.command()  # type: ignore
def main(
    max_errors: Annotated[
        int,
        Option(
            "-e",
            "--max-errors",
            help="Maximum number of errors allowed before stopping early.",
        ),
    ] = MAX_ERRORS,
    retry_rate: Annotated[
        int, Option("-r", "--retry-rate", help="Minutes to wait between requests.")
    ] = RETRY_RATE,
) -> None:
    error_count: int = 0
    while True:
        is_sold_out: bool | None = None

        try:
            is_sold_out = scraper.is_thorofare_net_soldout()
        except BaseException as err:
            logger.error(f"An error occurred while scraping the product page: {err}.")
            error_count += 1
            if error_count >= max_errors:
                logger.error(f"Max errors of {max_errors} reached. Stopping.")

        match is_sold_out:
            case None:
                ...
            case True:
                logger.info("The Thorofare Net is still sold out.")
            case False:
                logger.info("The Thorofare Net is back in stock!")
                logger.info("Sending email.")
                email.send_email()
                logger.info("Email sent, breaking loop.")
                break

        sleep(retry_rate * 60)
