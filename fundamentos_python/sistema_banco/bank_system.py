from biblio import *


class Conta(object):

    def __init__(self, num, nome, valor):
        self.__num = num
        self.__nome = nome
        self.__saldo = valor

    def set_num(self, num):
        self.__num = num

    def get_num(self):
        return self.__num

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_saldo(self, valor):
        self.__saldo = valor

    def get_saldo(self):
        return self.__saldo

    def __str__(self):
        return f"Número da conta: {str(self.__num)} \nNome do titular:  {self.__nome} \nSaldo: {str(self.__saldo)} \n"


def mostra_menu():
    OPCOES = (0, 1, 2, 3, 4)
    opcao_ok = False
    while (not opcao_ok):
        print("\n--- Sistema Bancário ---")
        print("1 - Inclusão")
        print("2 - Alteração")
        print("3 - Listar")
        print("4 - Exclusão")
        print("0 - Sair")
        opcao = entra_numero("Entre com a opção: ")
        if (opcao not in OPCOES):
            print("Opção inválida")
        else:
            opcao_ok = True
    return opcao


def pesquisa_contas(contas, num_conta):
    achou = False
    cont = None
    for conta in contas:
        if (conta.get_num() == num_conta):
            achou = True
            cont = conta
            print(conta)
    return achou, cont


def incluir(contas):
    nova_conta = True
    num_conta = entra_numero("Entre com o número da conta: ")
    achou, conta = pesquisa_contas(contas, num_conta)
    if (achou):
        print("Erro: conta já existe")
        return
    nome = input("Entre com o nome: ")
    try:
        saldo = float(input("Entre com o saldo: "))
        contas.append(Conta(num_conta, nome, saldo))

    except:
        print("Erro ao criar conta. Verifique os valores informados e tente novamente.")
    
    for conta in contas:
        print(contas[-1])

    return


def alterar(num_conta):
    num_conta = entra_numero("Entre com o número da conta: ")
    achou, conta = pesquisa_contas(contas, num_conta)
    if (achou):
        conta.set_num(input("Novo número: "))
        conta.set_nome(input("Novo nome: "))
        conta.set_saldo(input("Novo saldo: "))



def excluir(conta):
    num_conta = entra_numero("Entre com o número da conta: ")
    achou, conta = pesquisa_contas(contas, num_conta)

    print(conta)

    if achou:
        contas.remove(conta)

    return


def listar(contas):
    for conta in contas:
        print("")
        print(conta)

    return


def sair():
    print("\nFim da execução\n")


contas = []

acoes = (
    sair,
    incluir,
    alterar,
    listar,
    excluir
)

while True:

    opcao = mostra_menu()
    if opcao == 0:
        acoes[opcao]
        break
    else:
        acoes[opcao](contas)
        print("\nOperação realizada com sucesso!")
        # listar(contas)


print("\nFim da execução")
