participantes = []

def entrar_dados_participantes():

  for x in range(5):
    nome = input(f"Informe nome do {x+1}º participante: ")
    nota = float(input(f"Informe nota do {x+1}º participante:"))
    if nota >= 0 and nota <= 10:
      add_nota(nome, nota)
    else:
      print("Nota inválida.")
      return

  selecionar_melhor(participantes)     

def add_nota(nome, nota):

  participante = {
    'nome': nome,
    'nota': nota
  }

  participantes.append(participante)

def selecionar_melhor(participantes):
  maior_nota = 0
  vencedor = []

  for participante in participantes:
    if participante['nota'] > maior_nota:
      maior_nota = participante['nota']
      vencedor = participante
      
  print(f"O(a) vencedor(a) foi {vencedor['nome']} com nota {vencedor['nota']}!")

entrar_dados_participantes()