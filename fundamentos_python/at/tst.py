r = [[101, 10], [50, 50], [101, 50]]

# Verifica se o último elemento aparece na posição de um
# elemento que já existe. Caso apareça, elimina os dois.

for x in range(len(r)-1):
    if r[x][0]+50 >= r[-1][0] and r[x][1]+50 >= r[-1][1]:
        r.remove(r[-1])
        break
    else:
        print(False)

print(r)