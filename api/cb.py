import requests
from bs4 import BeautifulSoup
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
    'upgrade-insecure-requests': '1',
    'dnt': '1'
}


def fetch_price(url):
    with requests.Session() as session:
        post = session.get(url, headers=headers)
        soup = BeautifulSoup(post.text, 'html.parser')

    try:
        price = soup.find("span", {"class": "regPrice"}).contents[0]
        time.sleep(30)
        return price
    except:
        time.sleep(30)
        return 'Blocked my host'


while(True):
    print(fetch_price(
        'https://www.crateandbarrel.com/zuma-expandable-dining-table/s100543'))
