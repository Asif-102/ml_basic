import requests
from bs4 import BeautifulSoup

text = requests.get('https://en.wikipedia.org/wiki/IPhone', auth=('user', 'pass')).text
soup = BeautifulSoup(text, 'lxml')

print(soup)