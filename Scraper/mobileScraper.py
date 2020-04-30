import requests
from bs4 import BeautifulSoup
import Tender


class mobileScraper():
    def __init__(self, url: str):
        self.url = url
        self.session = requests.Session()
        self.source = self.session.get(url).text
        self.soup = BeautifulSoup(self.source, "html.parser")
        print(self.soup.prettify())

    def scrape(self) -> Tender:
        tender = Tender()
        return tender

