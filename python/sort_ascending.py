list_size = int(input('Números: '))

numbers = []

for i in range(list_size):
    numbers.append(int(input(f'Número {i}: ')))


def sort_ascending(numbers):
    numbers.sort()
    print(numbers)


sort_ascending(numbers)