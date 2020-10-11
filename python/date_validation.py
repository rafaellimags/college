import calendar


def get_date():
    print('Digite uma data no formato aaaa/m/dd')
    year = int(input('Ano: '))
    month = int(input('Mês: '))
    day = int(input('Dia: '))

    validate_date(year, month, day)


def validate_date(year, month, day):
    weekday, total_days = calendar.monthrange(year, month)
    if day > total_days:
        print('Data inválida')
        return

    weekday_name = calendar.day_name[weekday]
    month_name = calendar.month_name[month]
    print(f'{weekday_name}, {month_name} {day} {year}')


get_date()
