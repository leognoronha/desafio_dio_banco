menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[x] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

  opcao = input(menu)

  if opcao == "1":
    valor_deposito = float(input (f"Insira um valor para depósito: "))

    if valor_deposito <= 0:
      print("Insira apenas valores positivos!")
    else:
      saldo += valor_deposito
      extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
      print(f"Valor do depósito de R${valor_deposito:.2f} realizado com sucesso!\nSeu saldo atual é de R${saldo:.2f}")

  elif opcao == "2":
    valor_saque = float(input (f"limite disponível para saque:{limite}\nInsira um valor para sacar: "))
    
    if numero_saques >= LIMITE_SAQUES:
      print("Número de saques diários excedidos!")
    elif  valor_saque > limite:
      print(f"Limite da conta excedido, o limite total para saque é: R${limite:.2f}")
    elif valor_saque <= 0:
      print("Não é possível realizar esse tipo de saque")  
    elif saldo < valor_saque:
      print("Saldo insuficiente!")
    else:
      saldo -= valor_saque
      numero_saques += 1
      extrato += f"Saque: R$ {valor_saque:.2f}\n"
      print(f"Saque de {valor_saque} realizado com sucesso!\nSeu saldo atual é de {saldo:.2f}")
  
  elif opcao == "3":
        print("########## EXTRATO ##########")
        print("Sem transações na conta." if not extrato else extrato)  
        print(f"\nSaldo atual: R${saldo:.2f}")
        print("##############################")


  elif opcao =="x":
    print("Obrigado por usar nosso sistema!")
    break
  
  else:
    print("Operação inválida! Selecione a operação desejada.")



  