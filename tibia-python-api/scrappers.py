import requests
from bs4 import BeautifulSoup

def getPageConent(url, reader):
    page = requests.get(url)
    parser = BeautifulSoup(page.content, 'html.parser')
    return reader(parser)
