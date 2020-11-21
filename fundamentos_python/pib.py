import matplotlib.pyplot as plt


def menu():
    print('# Selecione:')
    print('> 1 para busca individual do PIB de um país no ano')
    print('> 2 para listar a estimativa de variação do PIB entre 2013 e 2020')
    print('> 3 para gráfico da evolução do PIB de um país específico')
    selecao = input('\n> ')
    pegar_dados(selecao)


def pegar_dados(selecao):
    cabecalho, paises = preparar_dados()

    if selecao == '1':
        pais = input('\nInforme um país: ')
        ano = input('Informe um ano entre 2013 e 2020: ')
        mostrar_dados_pais(cabecalho, paises, pais, ano)
    elif selecao == '2':
        pais = input('\nInforme um país: ')
        filtrar_pais(cabecalho, paises, pais, selecao)
    else:
        pais = input('\nInforme um país: ')
        filtrar_pais(cabecalho, paises, pais, selecao)


def chamar_arquivo():
    return f"./data/PIBs.csv"


def preparar_dados():
    nome_arquivo = chamar_arquivo()
    arquivo = open(nome_arquivo, 'r', encoding='UTF-8')
    dados_crus = arquivo.read()
    linhas = dados_crus.splitlines()
    dados_crus_cabecalho = linhas[0]
    lista_cabecalho = dados_crus_cabecalho.split(";")
    dados_crus_paises = linhas[1:]
    lista_paises = []
    for pais in dados_crus_paises:
        pais = pais.split(';')
        lista_paises.append(pais)
    return lista_cabecalho, lista_paises


def mostrar_dados_pais(cabecalho, paises, str_pais, ano):
    cabecalho = cabecalho[0].split(',')
    coluna_paises = cabecalho.index('País')
    index_ano = 0
    try:
        index_ano = cabecalho.index(ano)
    except:
        print('Ano inválido')
        return

    for lst_pais in paises:
        lst_pais = lst_pais[coluna_paises].split(',')
        if lst_pais[coluna_paises].lower() == str_pais.lower():
            print(
                f'\nPIB {lst_pais[coluna_paises]} em {ano}: U${lst_pais[index_ano]} trilhões.')
            return

    print('Pais inválido')


def filtrar_pais(cabecalho, paises, str_pais, sel):
    cabecalho = cabecalho[0].split(',')
    index_coluna_pais = cabecalho.index('País')
    for pais in paises:
        pais = pais[index_coluna_pais].split(',')
        if pais[index_coluna_pais].lower() == str_pais.lower():
            if sel == '2':
                calcular_variacao_pib(pais)
            if sel == '3':
                mostrar_variacao_grafica(cabecalho[1:], pais[1:])
            return
    print('O país informado não existe na lista.')


def calcular_variacao_pib(pais):
    f_primeiro_pib = float(pais[1])
    f_ultimo_pib = float(pais[-1])
    variacao_pib = (f_ultimo_pib / f_primeiro_pib) - 1
    variacao_percentual_pib = f"{(variacao_pib * 100):.2f}%"
    print(f'Variação de {variacao_percentual_pib} entre 2013 e 2020')


def mostrar_variacao_grafica(anos, pibs):

    x = []
    y = []

    for ano in anos:
        x.append(int(ano))

    for pib in pibs:
        y.append(float(pib))

    plt.plot(x, y)
    plt.xlabel('Ano')
    plt.ylabel('PIB')
    plt.grid(True)
    plt.show()


menu()
