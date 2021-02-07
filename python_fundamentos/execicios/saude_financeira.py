def calc_balance():
    expenses = []
    while True:
        income = float(input('Renda mensal total: '))
        expenses.append(float(input('Gastos totais com moradia: ')))
        expenses.append(float(input('Gastos totais com educação: ')))
        expenses.append(float(input('Gastos totais com transporte: ')))
        if len(expenses) == 3:
            break
    dwell_exp = expenses[0] / income
    educ_exp = expenses[1] / income
    transp_exp = expenses[2] / income

    balance = [dwell_exp, educ_exp, transp_exp]

    show_health(income, balance)


def show_health(income, balance):
    if (balance[0] <= 0.3):
        print('Seus gastos estão dentro da margem recomendada.')
    else:
        print(
            f'Seus gastos totais com moradia comprometem {balance[0] * 100}% de sua renda total. O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {(income * 0.3):.2f}.')

    if (balance[1] <= 0.2):
        print('Seus gastos estão dentro da margem recomendada.')
    else:
        print(
            f'Seus gastos totais com educação comprometem {balance[1] * 100}% de sua renda total. O máximo recomendado é de 20%. Portanto, idealmente, o máximo de sua renda comprometida com educação deveria ser de R$ {(income * 0.2):.2f}.')

    if (balance[2] <= 0.15):
        print('Seus gastos estão dentro da margem recomendada.')
    else:
        print(
            f'Seus gastos totais com moradia transporte {balance[2] * 100}% de sua renda total. O máximo recomendado é de 15%. Portanto, idealmente, o máximo de sua renda comprometida com transporte deveria ser de R$ {(income * 0.15):.2f}.')

    print(balance)


calc_balance()
