address = int(input('Primeiros números: '))


def check_ip_class(address):
    if address >= 0 and address <= 127:
        print('IP classe A')
    elif address > 127 and address <= 191:
        print('IP classe B')
    elif address > 191 and address <= 223:
        print('IP classe C')
    elif address > 223 and address <= 239:
        print('IP classe D')
    elif address > 239 and address <= 255:
        print('IP classe E')
    else:
        print('Endereço de IP inválido')


check_ip_class(address)
