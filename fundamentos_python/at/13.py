import requests
import re
from collections import Counter
from bs4 import BeautifulSoup

url = 'http://brasil.pyladies.com/about'

request = requests.get(url)
request.encoding = request.apparent_encoding
bs = BeautifulSoup(request.text, "lxml")

ladies = 0
words = []
sections = []


for about in bs.find_all('p', class_='about-text'):
    ladies += about.text.lower().count('ladies')
    for word in about.text.split():
        word = re.sub('\W+', '', word)
        words.append(word.lower())
    
total_words = len(words)

print(f'Total de palavras: {total_words}')

same_words = dict(Counter(words))

for word, occurrency in same_words.items():
    if occurrency == 1:
        print(f'{word} apareceu {occurrency} vez.')
    else:
        print(f'{word} apareceu {occurrency} vezes.')
