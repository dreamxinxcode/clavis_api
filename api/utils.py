import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
    'upgrade-insecure-requests': '1',
    'dnt': '1'
}


def fetch_price(product):
    retailer = product.retailer

    with requests.Session() as session:
        post = session.get(product.url, headers=headers)
        soup = BeautifulSoup(post.text, 'html.parser')

    if (retailer == 'WAYFAIR'):
        price = soup.find("span", {"class": "notranslate"}).contents[0]
    if (retailer == 'EQ3'):
        pass
    if (retailer == 'ELTE'):
        price = soup.find("span", {"class": "pdp-priceActual"}).contents[0]
    if (retailer == 'CRATE_&_BARREL'):
        price = soup.find("span", {"class": "regPrice"}).contents[0]
    if (retailer == 'BOUCLAIR'):
        price = soup.find_all("span", {"class": "value"})[1].text
    if (retailer == 'ARTICLE'):
        price = soup.find("span", {"class": "regularPrice"}).contents[0]

    return price
