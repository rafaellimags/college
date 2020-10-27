print('Informe quantos anos, meses e dias você tem.')

age = []

age.append(int(input('Anos: ')))
age.append(int(input('Meses: ')))
age.append(int(input('Dias: ')))

print(age)


def calculate_total_days(age):
    years_to_days = age[0] * 365
    months_to_days = age[1] * 30
    days = age[2]

    total_days = years_to_days + months_to_days + days

    show_output_message(total_days)


def show_output_message(days):
    print(f'O total de dias de vida é de: {days}.')


calculate_total_days(age)
