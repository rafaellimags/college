print("🗳 Deseja iniciar a sessão? (Sim/Nao)")

def registrar_voto():
  voto = int(input("Digite o número do candidato: "))
  print("Voto registrado com sucesso!")

def validar_idade():
  idade = int(input("Informe sua idade: "))
  
  if idade < 16:
    print("Não tem direito a voto.")
  elif (idade >= 16 and idade < 18) or idade >= 70:
    print("Voto facultativo. Deseja votar?\nPara sim, digite 1.\nPara não, digite 0")
    resposta = bool(int(input()))
    if resposta == True:
      registrar_voto()
  else:
    print("Voce precisa votar. Por favor, digite um número")
    registrar_voto()

def iniciar_sessao():

  while True:
    iniciar = input().lower()
    if iniciar == "sim":
      validar_idade()
      print("Sessão encerrada.")
      break
    elif iniciar == "nao":
      print("Sessão encerrada.")
      break
    else:
      print("Não entendi. Por favor, repita sua resposta.")

iniciar_sessao()