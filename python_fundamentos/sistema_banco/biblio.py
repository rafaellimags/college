def entra_numero(msg):

    num_ok = False
    while (not num_ok):
        try:
            num = int(input(msg))
            num_ok = True
        except:
            print("Erro: número inválido")
    return num