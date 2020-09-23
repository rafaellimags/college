import matplotlib.pyplot as plt

def get_entry_data():
    initial_inv = float(input('Valor inicial: '))
    monthly_prof = float(input('Rendimento (a.m.): ')) / 100
    monthly_inv = float(input('Aporte mensal: '))
    terms = int(input('Período de aplicação (meses): '))

    calc_final_balance(initial_inv, monthly_prof, monthly_inv, terms)


def calc_final_balance(initial_inv, monthly_prof, monthly_inv, terms):
    accumulated_prof = initial_inv
    months = []
    balance = []

    for mes in range(terms):
        months.append(mes)
        balance.append(accumulated_prof)
        accumulated_prof = monthly_inv + \
            (accumulated_prof * (1 + monthly_prof))

    show_final_balance(accumulated_prof, months, balance)


def show_final_balance(accumulated_prof, months, balance):
    plt.plot(months, balance)
    plt.title('Evolução patrimonial')
    plt.xlabel('Meses')
    plt.ylabel('Saldo (R$)')
    plt.grid(True)
    plt.show()
    print(f'Saldo final: R$ {accumulated_prof:.2f}')
    print(f'Período total da aplicação: {len(months)} meses')


get_entry_data()
