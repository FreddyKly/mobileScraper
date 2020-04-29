import requests


class mobileScraper():
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()