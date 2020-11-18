import random

throws = []
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

for _ in range(10):

    throw = random.randint(1, 6)
    throws.append(throw)

    
for number in throws:
    if number == 1:
        one = one + 1
    elif number == 2:
        two += 1
    elif number == 3:
        three += 1
    elif number == 4:
        four += 1
    elif number == 5:
        five += 1
    else:
        six += 1



print(throws)
print(f'Numero 1: {one}')
print(f'Numero 2: {two}')
print(f'Numero 3: {three}')
print(f'Numero 4: {four}')
print(f'Numero 5: {five}')
print(f'Numero 6: {six}')