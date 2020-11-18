import random

rolls = []


def catch(roll):
    rolls.append(roll)


def roll():
    for _ in range(10):
        roll = random.randint(1, 6)
        catch(roll)


def count():
    for i in range(1, 7):
        occurr = rolls.count(i)
        print(f'Número {i}: {occurr} vezes.')


roll()
print(f'\nNúmeros jogados: {rolls}\n')
count()
