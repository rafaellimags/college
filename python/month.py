print('\nInforme um mês de 1 a 12')
month = int(input('Mês do ano: '))


def check_month(month):
    months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
              'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    print(f'{months[month -1]}\n')


def validate_month(month):

    if month < 1 or month > 12:
        print('Data inválida.\n')
        return

    check_month(month)


validate_month(month)
