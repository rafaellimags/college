import random

t = int(input('\nTamanho da lista: '))


def append_numbers():
    int_arr = []
    for i in range(t):
        int_arr.append(random.randint(0, 10))

    return int_arr


def zero_count(int_arr):
    z_count = 0

    for x in range(t):
        if int_arr[x] == 0:
            z_count += 1

    return z_count


def show_msgs():
    int_arr = append_numbers()
    z_amount = zero_count(int_arr)
    print(f'\nLista: {int_arr}')
    print(f'Zeros na lista: {z_amount}\n')


show_msgs()
