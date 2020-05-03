import requests
from Scraper.mobileScraper import MobileScraper
from UrlBuilder.UrlBuilder import UrlBuilder


def run():
    url = UrlBuilder('Mitsubishi', '2000', 'SportsCar', None, None, '131').builder()
    mobScraper = MobileScraper(url)
    mobScraper.scrape()