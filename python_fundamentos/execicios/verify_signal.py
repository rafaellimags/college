number = int(input('Número: '))

def verify_signal(number):
    if number > 0:
        print('Número positivo')
    elif number < 0:
        print('Número negativo')
    else:
        print('Zero')


verify_signal(number)