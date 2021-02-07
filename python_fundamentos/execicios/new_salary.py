value = float(input('Salário: '))


def calculate_raise(sal):
    if sal > 0 and sal <= 1000:
        sal = sal * 1.3
    elif sal > 1000 and sal <= 2000:
        sal = sal * 1.25
    elif sal > 2000 and sal <= 3000:
        sal = sal * 1.2
    elif sal > 3000 and sal <= 4000:
        sal = sal * 1.15
    else:
        sal = sal * 1.1

    sal = f'{sal:.2f}'.replace('.', ',')
    print(f'Novo salário com aumento é de R$ {sal}')


calculate_raise(value)
