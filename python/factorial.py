print('\n' + '#' * 30 + '\n')

number = int(input('Informe um número: '))

def calculate_factorial(n):
    fact = 1
    for i in range(n, 1, -1):
        fact = fact * i

    print(fact)


calculate_factorial(number)
