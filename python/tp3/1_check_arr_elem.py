lst = []

for x in range(1, 6):
    lst.append(x)

print(f'\nLista: {lst}')

for i in range(len(lst)-1):
    if i == 3 or i == 6:
        lst.remove(i)


print(f'Três foi removido: {lst}')
print(f'Tamanho da lista: {len(lst)} elementos.')
lst.append(6)
print(f'Seis adicionado: {lst}\n')
