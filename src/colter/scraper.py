"""Web scraping module."""

import requests
from bs4 import BeautifulSoup, Tag
from loguru import logger

BASEURL = "https://colterbackcountry.com/products/thorofare-net"


def _extract_price_badge_data(soup: BeautifulSoup) -> dict[str, list[str]] | None:
    price = soup.find(class_="price")

    if price is None:
        logger.error("Failed to find price.")
        return None

    if not isinstance(price, Tag):
        logger.error(f"Price is a '{type(price)}' not a 'Tag'.")
        return None

    badges = {}
    for badge in price.findAll(class_="badge"):
        badges[badge.text.strip()] = badge.attrs["class"]

    return badges


def is_thorofare_net_soldout() -> bool:
    """Scrape the Thorofare Net's product page."""
    logger.info("Fetching product page.")
    res = requests.get(BASEURL)

    if res.status_code != 200:
        logger.error(f"Failed to fetch product pag: '{res.status_code}'.")
        res.raise_for_status()

    logger.info("Successfully fetched product page.")

    logger.info("Parsing product page.")
    soup = BeautifulSoup(res.content, "html.parser")

    price = soup.find(class_="price")
    logger.debug(f"Price:\n{price}")
    price_attrs = price.attrs["class"]
    logger.debug(f"Price class attributes: {price_attrs}")

    return any("sold-out" in attr for attr in price_attrs)
