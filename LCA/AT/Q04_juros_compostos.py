# valor de aplicação inicial
# percentual de rendimento mensal
# valor de aporte mensal

# rendimento total (calculado)

def get_entry_data():
    initial_inv = float(input('Valor inicial: '))
    monthly_prof = float(input('Rendimento (a.m.): ')) / 100
    monthly_inv = float(input('Aporte mensal: '))
    terms = int(input('Período de aplicação (meses): '))

    final_balance(initial_inv, monthly_prof, monthly_inv, terms)


def final_balance(initial_inv, monthly_prof, monthly_inv, terms):
    accumulated_prof = initial_inv
    for mes in range(terms):
        accumulated_prof = monthly_inv + (accumulated_prof * (1 + monthly_prof))

    print(f"{accumulated_prof:.2f}")


get_entry_data()

