import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
    'upgrade-insecure-requests': '1',
    'dnt': '1'
}


def fetch_wayfair_price(url):
    with requests.Session() as session:
        post = session.get(url, headers=headers)
        soup = BeautifulSoup(post.text, 'html.parser')
    print(soup.find("span", {"class": "notranslate"}).contents[0])


fetch_wayfair_price(
    'https://www.wayfair.ca/furniture/pdp/mistana-katarina-5-piece-extendable-solid-wood-dining-set-mitn2584.html')
