import requests
from bs4 import BeautifulSoup

url = 'https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html'

html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')
print()
for title in soup.find_all('div', class_='titulo'):
    for cell in title.find_all('div', class_='celula'):
        print('{:25}'.format(cell.string), end='')


for body in soup.find_all('div', class_='linha'):
    print()
    for cell in body.find_all('div', class_='celula'):
        print('{:25}'.format(cell.string), end='')

