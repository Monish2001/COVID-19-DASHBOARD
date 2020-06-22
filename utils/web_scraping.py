import requests
from bs4 import BeautifulSoup


def scraping():
    source = requests.get('https://www.mygov.in/covid-19').text
    soup = BeautifulSoup(source, 'lxml')
    return soup
