import urllib.request as ul
from bs4 import BeautifulSoup as Soup


def treasury_yield():
    url = 'https://www.cnbc.com/quotes/US10Y'
    pagesoup = get_page_soup(url)
    treasury_yield = float(pagesoup.find('span', {'class': 'QuoteStrip-lastPrice'}).contents[0][:-1])
    return treasury_yield


def get_page_soup(url):
    req = ul.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    client = ul.urlopen(req)
    htmldata = client.read()
    client.close()
    return Soup(htmldata, "html.parser")