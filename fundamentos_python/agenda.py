# Definir função de exibição do menu do sistema
def exibir_menu():
    # Document string - Serve para fazer uma documentação do código
    ''' Exibe o menu de opções do sistema. '''
    print("*** Agenda de Contatos ***")
    print("(1) Criar novo contato")
    print("(2) Listar todos os contatos")
    print("(3) Buscar contato")

    # Chamada do menu
exibir_menu()


def cadastrar_contato(nome, telefone, email, arquivo_agenda):
    ''' documentar '''
    # Abrir arquivo em modo append
    agenda = open(arquivo_agenda, 'a')
    # escrever , na agenda, os dados do contato
    agenda.write(f"{nome}, {telefone}, {email}\r")
    agenda.close()

agenda = open("data/agenda.csv", "w")
agenda.write("Nome,Telefone,Email\r")
agenda.close()

cadastrar_contato("Rafael", "81999999999",
                  "rafael@exemplo.com.br", "data/agenda.csv")
cadastrar_contato("Mariana", "41999999999",
                  "mariana@exemplo.com.br", "data/agenda.csv")
cadastrar_contato("Marina", "21999999999",
                  "marina@exemplo.com.br", "data/agenda.csv")

agenda = open("data/agenda.csv")
contatos = agenda.readlines()
for contato in contatos:
    print(contato)


def listar_contatos(arquivo_agenda):
    ''' Lista nome, telefone e email de cada contato na agenda '''
    # Abrir agenda para leitura
    agenda = open(arquivo_agenda, "r")
    # Ler todo o conteúdo da agenda
    contatos = agenda.read()  # Contatos é uma string contendo todos os dados
    # Sobrescrever contatos transformando-o em elementos de uma lista
    # Cada elemento da lista será uma das linhas da agenda
    contatos = contatos.splitlines()  # Contatos é uma lista
    agenda.close()

    # Percorrer a lista de contatos
    for contato in contatos:
        contato = contato.split(',')  # Contato vira uma lista
        nome = contato[0]
        telefone = contato[1]
        email = contato[2]
        print(f"{nome:<10}\t{telefone:>10}\t{email:<30}")


def buscar_contato(busca, arquivo_agenda):
    resultados = 0
    agenda = open(arquivo_agenda)
    contatos = agenda.read()
    agenda.close()
    contatos = contatos.splitlines()
    contatos = contatos[1:]
    for contato in contatos:
        contato = contato.split(',')
        nome = contato[0]
        telefone = contato[1]
        email = contato[2]
        if busca.lower() in nome or busca.lower() in telefone or busca.lower() in email:
            print(f"{nome:30} {telefone:15} {email:50}")
            resultados += 1
    if resultados > 1:
        print(f"\nForam encontrados {resultados} resultado(s).")
    elif resultados == 1:
        print(f"\nFoi encontrado {resultados} resultado.")
    else:
        print(f"\nNenhum resultado foi encontrado.")


buscar_contato("mARi", "data/agenda.csv")

arquivo_agenda = input("Informe o arquivo de agenda: ")
while True:
    exibir_menu()
    print("**********************************\n")
    opcao = int(input("Selecione a opção desejada (digite 9 para sair): "))
    print("**********************************\n")
    if opcao == 1:
        print("Cadastro de novo contato.")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        cadastrar_contato(nome, telefone, email, arquivo_agenda)
        print(f"\nContato {nome} cadastrado com sucesso.")
        print("**********************************\n")
    elif opcao == 2:
        print("Listar todos os contatos.")
        listar_contatos(arquivo_agenda)
        print("**********************************\n")
    elif opcao == 3:
        print("Buscar contato.")
        busca = input("Informe o parâmetro de busca: ")
        buscar_contato(busca, arquivo_agenda)
        print("**********************************\n")
    elif opcao == 9:
        break
    else:
        print("Opção inválida.")
        print("**********************************\n")
