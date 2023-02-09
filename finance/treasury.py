import urllib.request as ul
from bs4 import BeautifulSoup as Soup


class Treasury:
    def __init__(self, url):
        self.__url = url  # 'https://www.cnbc.com/quotes/US10Y'

    def treasury_yield(self):
        pagesoup = self.get_page_soup()
        treasury_yield = float(pagesoup.find('span', {'class': 'QuoteStrip-lastPrice'}).contents[0][:-1])
        return treasury_yield

    def get_page_soup(self):
        req = ul.Request(self.__url, headers={'User-Agent': 'Mozilla/5.0'})
        client = ul.urlopen(req)
        htmldata = client.read()
        client.close()
        return Soup(htmldata, "html.parser")
