print('\n' + '#' * 30 + '\n')

number = int(input('Informe um número: '))


def calculate_factorial(n):
    fact = 1

    if n == 0:
        return 1
    else:
        for i in range(n, 1, -1):
            fact = fact * i

    return fact


print(calculate_factorial(number))
