letter = input('Letra: ').lower()


def check_letter(letter):
    vowel_list = ['a', 'e', 'i', 'o', 'u']

    for vowel in vowel_list:
        if letter == vowel:
            print(f'{letter} é vogal')
            return

    print(f'{letter} é consoante')


check_letter(letter)
