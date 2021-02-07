
contacts = []

def show():
    print(contacts)
    print('\n')


def insert():
    print('\nPara sair, digite /s')
    while True:
        contact = input('Nome: ')
        contacts.append(contact)

        if contact == '/s':
            contacts.pop()
            break

def remove():
    while True:
        print('\nPara sair, digite /s')
        print('Nome a ser removido:\n')
        contact = input('> ')
        if contact in contacts:
            contacts.remove(contact)
            print('Registro removido')

        if contact == '/s':
            break


def remove_all():
    contacts.clear()
    print('Todos os registros foram removidos')

def init():

    while True:
        print('\nEscolha uma opção:\n\n1 - Mostrar registros\n2 - Adicionar registro\n3 - Remover registro\n4 - Apagar lista\n0 - Sair\n')
        op = input('> ')
        print('')

        if op == '1':
            show()
        elif op == '2':
            insert()
        elif op == '3':
            remove()
        elif op == '4':
            remove_all()
        elif op == '0':
            break
        else:
            print('Opção inválida')


init()
