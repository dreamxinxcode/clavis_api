import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
    'upgrade-insecure-requests': '1',
    'dnt': '1'
}


def fetch_price(product):
    with requests.Session() as session:
        post = session.get(product.url, headers=headers)
        soup = BeautifulSoup(post.text, 'html.parser')
    if (product.retailer == 'WAYFAIR'):
        price = soup.find("span", {"class": "notranslate"}).contents[0]
    if (product.retailer == 'EQ3'):
        pass
    if (product.retailer == 'ELTE'):
        pass
    if (product.retailer == 'CRATE_&_BARREL'):
        pass
    if (product.retailer == 'BOUCLAIR'):
        price = soup.find_all("span", {"class": "value"})[1].text
    if (product.retailer == 'ARTICLE'):
        price = soup.find("span", {"class": "regularPrice"}).contents[0]
    time.sleep(.25)
    return price
