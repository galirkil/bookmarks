from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


def get_raw_html(url):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    raw_html = requests.get(url, headers=headers, timeout=20)
    return raw_html.text


def get_title(url):
    raw = get_raw_html(url)
    soup = BeautifulSoup(raw, 'html.parser')
    title = ''
    if soup.find_all('meta', property='og:title'):
        title = soup.find('meta', property='og:title')['content']
    elif soup.title:
        title = soup.title.text

    return title


def get_description(url):
    raw = get_raw_html(url)
    soup = BeautifulSoup(raw, 'html.parser')
    description = ''
    if soup.find_all('meta', property='og:description'):
        description = soup.find('meta', property='og:description')['content']
    elif soup.find_all('meta', attrs={'name': 'description'}):
        description = soup.find('meta', attrs={'name':'description'})['content']

    return description


def get_favicon_url(url):
    base_url = urlparse(url).netloc
    favicon_url = 'https://' + base_url + '/favicon.ico'
    return favicon_url
