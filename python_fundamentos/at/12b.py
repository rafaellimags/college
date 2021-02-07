import requests
from bs4 import BeautifulSoup

url = 'https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html'

html = requests.get(url).text

region = input('Sigla da Região: ')

soup = BeautifulSoup(html, 'html.parser')
print()
for title in soup.find_all('div', class_='titulo'):
    for cell in title.find_all('div', class_='celula'):
        print('{:25}'.format(cell.string), end='')

print()
for body in soup.find_all('div', class_='linha'):
    for cell in body.find_all('div', class_='celula'):
        if cell.string == region:
            for cell in body.find_all('div', class_='celula'):
                print('{:25}'.format(cell.string), end='')

