import requests
from bs4 import BeautifulSoup
from Tender.Tender import Tender


class MobileScraper:
    def __init__(self, url: str):
        self.url = url
        self.session = requests.Session()
        headers = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        self.source = self.session.get(url, headers = headers).text
        self.soup = BeautifulSoup(self.source, "html.parser")
        print(self.soup.prettify())

    def scrape(self) -> Tender:
        tender = Tender()
        return tender

