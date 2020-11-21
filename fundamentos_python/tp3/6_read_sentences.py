print('\nComeçe a digitar abaixo:\n')

words = []

while True:
    sentences = input('> ')

    words.append(sentences)

    if sentences == 'sair':

        print('\nEstas palavras contém "eu":\n ')

        for word in words:
            if 'eu' in word:
                print(word)

        words.pop()
        print('\nPalavras usadas:\n')
        print(words)
        break

