int_arr = []

while True:
    num_in = int(input(f'Números inteiros: '))
    int_arr.append(num_in)
    print(int_arr)
    if len(int_arr) == 4:
        print('Fim da execução\n')
        break