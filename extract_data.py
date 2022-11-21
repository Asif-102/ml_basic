import requests
from bs4 import BeautifulSoup

text = requests.get('https://en.wikipedia.org/wiki/IPhone', auth=('user', 'pass')).text
soup = BeautifulSoup(text, 'lxml')

tables = soup.find('table', class_='wikitable')
rows = tables.find_all('tr')[1:]

print(rows)