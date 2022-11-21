import requests

r = requests.get('https://en.wikipedia.org/wiki/IPhone', auth=('user', 'pass'))

print(r.text)