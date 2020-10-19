option = input('Escolha uma opção:\n\n1 - Encontrar o elemento na tupla\n2 - Dividir uma tupla\n3 - Excluir elemento da tupla\n4 - Inverter elementos da tupla\n\n')

def find():
    e = input('Elemento: ')

    t = ('Azul', 'Vermelho', 'Verde')


    def find_element(e, t):
        if e in t:
            return t.index(e)


    print('O índice do elemento é o', find_element(e, t))


def split():

    t = (1, 2, 3, 4, 5, 6)

    def split_tuple(t):

        if (int(len(t)%2) == 0):
            size_each = int(len(t)//2)
            t_result_1 = t[:size_each]
            t_result_2 = t[size_each:]
        else:
            size_each = int(len(t)//2)
            t_result_1 = t[:size_each]
            t_result_2 = t[size_each:-1]

        return print(f'Tupla 1: {t_result_1}\nTupla 2: {t_result_2}')


    split_tuple(t)


def remove():

    val = int(input('Elemento que será removido: '))

    t = (1, 2, 3, 4, 5)

    print(f'Tupla original {t}')


    def remove_element(val, t):

        t = t[:val - 1] + t[val:]

        return t


    print('Nova tupla:', remove_element(val, t))

def revert():

    t = (1, 2, 3, 4, 5, 6)

    def revert_tuple(t):
        return t[::-1]

    print(f'Normal: {t}\nRevertido:', revert_tuple(t))


if option == '1':
    find()
elif option == '2':
    split()
elif option == '3':
    remove()
elif option == '4':
    revert()
else:
    print('Função não existe')