amount = int(input('Quantos números deseja comparar?: '))
numbers = []

for i in range(amount):
    numbers.append(int(input(f'Número {i}: ')))

def verify_largest(numbers):
    largest = 0
    for number in numbers:
        if number > largest:
            largest = number
    
    print(f'O maior número é: {largest}')
         

verify_largest(numbers)