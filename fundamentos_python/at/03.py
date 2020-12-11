def multiply(b, e):
    if e == 1:
        return b
    if e == 0:
        return 1
    else:
        return b * multiply(b, e-1)

b = int(input("Base: "))
e = int(input("Expoente: "))

print('Resultado: ', multiply(b, e))