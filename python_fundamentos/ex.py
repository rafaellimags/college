class Pessoa(object):

    def __init__(self, andar, falar):
        self.__andar = andar

    # def get_andar(self):
    #     return "Andando..."

    def __str__(self):
        return self.__andar


pessoas = []
pessoas.append(Pessoa("Andando"))
for pessoa in pessoas:
    print(pessoa)

# class Conta(object):

#     def __init__(self, num, nome, valor):
#         self.__num = num
#         self.__nome = nome
#         self.__saldo = valor

#     def set_num(self, num):
#         self.__num = num

#     def get_num(self):
#         return self.__num

#     def set_nome(self, nome):
#         self.__nome = nome

#     def get_nome(self):
#         return self.__nome

#     def set_saldo(self, valor):
#         self.__saldo = valor

#     def get_saldo(self):
#         return self.__saldo

#     # Sobreescrita = override
#     def __str__(self):
#         return str(self.get_num()) + " " + self.get_nome() + " " + str(self.get_saldo())

# contas = []
# contas.append(Conta(23, "Rafael", 100))

# for conta in contas:
#     print(conta)