number = int(input('Número: '))


def verify_odd_even(number):
    if number % 2 == 0:
        print(f'Número {number} é par')
        return

    print(f'Número {number} é ímpar')


verify_odd_even(number)
