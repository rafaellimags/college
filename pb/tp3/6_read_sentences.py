print('\nComeçe a digitar abaixo:\n')

text = []

while True:
    sentences = input('> ')

    text.append(sentences)

    if sentences == 'sair':
        text.pop()
        print(text)
        break

