last_number = int(input('Informe o valor final: '))


def sum_all(last_number):
    total = 0
    for i in range(1, last_number + 1):
        total = i + total

    show_message(total)


def show_message(total):
    print(f'A soma de todos os números é: {total}')


sum_all(last_number)
