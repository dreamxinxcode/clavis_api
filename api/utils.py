import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}


def fetch_wayfair_price(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    print(soup)
