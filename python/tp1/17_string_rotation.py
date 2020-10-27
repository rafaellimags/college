stg = input('Digite alguma coisa: ')
pos = int(input('Indice de rotação '))

ns = stg[pos:] + stg[:pos]

print(ns)