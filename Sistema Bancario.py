menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "1":
       dinheiro = float(input("informe o valor do depósito: "))
       
       if dinheiro > 0:
           saldo += dinheiro
           extrato += f"Depósito: R$ {dinheiro:.2f}\n"
           
           
       else:
        print("Operação falhou, tente novamente outro valor!")
           
    elif opcao == "2":
        dinheiro = float(input("informe o valor do saque: "))

        sem_dinheiro = dinheiro > saldo

        sem_limite = dinheiro > limite

        saques_limite = numero_saques > LIMITE_SAQUES

        if sem_dinheiro:
            print("Operação falhou, ta sem grana!")

        elif sem_limite:
            print("Operação falhou, valor maior que o limite!")

        elif saques_limite:
            print("Operação falhou, limite diário atingido!")
        
        elif dinheiro > 0:
            saldo -= dinheiro
            extrato += f"Saque: R$ {dinheiro:.2f}\n"
            numero_saques += 1

        else:
            print("O valor informado é invalido")

    elif opcao == "3":
        print("Não foi realizado nenhuma movimentação." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
    
    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")