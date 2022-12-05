import requests
from bs4 import BeautifulSoup

text = requests.get('https://en.wikipedia.org/wiki/IPhone', auth=('user', 'pass')).text
soup = BeautifulSoup(text, 'lxml')

tables = soup.find('table', class_='wikitable')
rows = tables.find_all('tr')[1:]

for row in rows:
    data = row.find_all(['th', 'td'])
    try:
        version_text = data[0].a.text.split(' ')[1]
        version = re.sub(r"\D", "", version_text)
        print(version)
        price_text = data[-1].text.split('/')[-1]
        print(price_text)
    except:
        pass
# test