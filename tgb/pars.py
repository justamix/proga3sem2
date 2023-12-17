import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://www.anekdot.ru/id/10034")
html = BS(r.content, 'html.parser')

anekdot_text = html.find('div', class_='text').get_text(strip=True)
print(anekdot_text)