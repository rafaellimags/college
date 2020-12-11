t_int = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

t_evn = []
t_odd = []


def check_type(t_int):
    for num in t_int:
        if num % 2 == 0:
            t_evn.append(num)
        else:
            t_odd.append(num)


check_type(t_int)
print('Pares: ', t_evn)
print('Ímpares: ', t_odd)
