print("CONSUMO 🧾\n")

def validar_entradas():
  while True:
 
    total_pessoas = int(input("Informe o total de pessoas: "))
    total_consumo = float(input("Informe o valor total do consumo: "))
 
    if total_pessoas > 0 and int(total_consumo) > 0:
      while True:
        taxa_servico = float(input("Informe o percentual do serviço, entre 0 e 100: "))
        if taxa_servico > 0 and taxa_servico <= 100:
          dados_entrada = [total_pessoas, total_consumo, taxa_servico]
          return dados_entrada
        print("Valor da taxa de serviço Inválido.")
 
    print("A quantidade de pessoas e valor de consumo devem ser maiores que 0.")

def calcular_total(entradas):
  
  taxa_serv_calc = 1 + (entradas[2]/100)
  total_pessoas = entradas[0]
  total_consumo = entradas[1]
 
  valor_conta = total_consumo * taxa_serv_calc
  valor_parcial = valor_conta / total_pessoas
  f_valor_parcial = f"{valor_parcial:.2f}"
  fs_valor_parcial = f_valor_parcial.replace('.', ',')
  print(f'-----------------------\nDividindo a conta por {total_pessoas} pessoa(s), cada pessoa deverá pagar R$ {fs_valor_parcial}.')

calcular_total(validar_entradas())