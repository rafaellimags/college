num = int(input('Número: '))

def calculate_factorial(n):
    fact = 1

    if n == 0:
        return 1
    else:
        while n > 1:
            fact = fact * n
            n = n - 1

    return fact

print(calculate_factorial(num))