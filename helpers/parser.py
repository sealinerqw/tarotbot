from bs4 import BeautifulSoup
import re
import requests


def parse_general_horoscope():
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0'})
    url = requests.get('https://horo.mail.ru/prediction/', headers=headers)
    soup = BeautifulSoup(url.text, 'html.parser')
    title = soup.find('h1', {'data-qa': 'Title'}).getText()
    content = soup.find('main', {'data-qa': 'ArticleLayout'}).getText()
    result = BeautifulSoup(content, 'html.parser')
    return result


def parse_sign_horoscope(sign):
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0'})
    url = requests.get('https://horo.mail.ru/prediction/' + sign + '/today', headers=headers)
    soup = BeautifulSoup(url.text, 'html.parser')
    title = soup.find('h1', {'data-qa': 'Title'}).getText()
    content = soup.find('main', {'data-qa': 'ArticleLayout'}).getText()
    result = BeautifulSoup(content, 'html.parser')
    return result

