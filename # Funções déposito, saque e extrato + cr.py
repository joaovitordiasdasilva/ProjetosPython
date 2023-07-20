# Funções déposito, saque e extrato + criar duas novas (cadastrar usuário e conta bancária)

# 3 saques diários, não podendo passar de 500 cada um.
customers = []
account_number = 1
accounts = []
statement = []

def deposit():
    conta = int(input('Digite o número da conta: '))
    for i in accounts:
        if i['Conta'] == conta:
            value = float(input('Digite o valor do depósito: '))
            i['Saldo'] += value
            print('Depósito realizado com sucesso!')
            statement.append({'Conta': conta, 'Valor': value, 'Tipo': 'Depósito'})
            break
        else:
            print('Conta não encontrada.')

def debit():
    conta = int(input('Digite o número da conta: '))
    for i in accounts:
        if i['Conta'] == conta:
            daily_limit = i['Saques']
            balance = i['Saldo']
            break
    else:
        print('Conta não encontrada.')
        return

    value = float(input('Digite o valor do saque: '))
    if value > 500:
        print('O valor máximo de saque é de R$ 500,00.')
    elif daily_limit == 0:
        print('Você atingiu o limite de saques diários.')
    elif value > balance:
        print('Saldo insuficiente.')
    else:
        i['Saldo'] -= value  
        i['Saques'] -= 1  
        print('Saque realizado com sucesso!')
        statement.append({'Conta': conta, 'Valor': value, 'Tipo': 'Saque'})

def statements():
    conta = int(input('Digite o número da conta: '))
    if conta not in [i['Conta'] for i in accounts]:
        print('Conta não encontrada.')
        return

    for i in accounts:
        if i['Conta'] == conta:
            balance = i['Saldo']  # Declare and initialize 'balance' variable
            break
    else:
        print('Conta não encontrada.')
        return

    if len(statement) == 0:
        print('Não foram realizadas movimentações.')
    else:
        for i in statement:
            if i['Conta'] == conta and i['Tipo'] == 'Depósito':
                print('Depósito realizado: R$ {:.2f}'.format(i['Valor']))
            elif i['Conta'] == conta and i['Tipo'] == 'Saque':
                print('Saque realizado: R$ {:.2f}'.format(i['Valor']))
    print('Saldo atual: R$ {:.2f}'.format(balance))

def client():
    global customers
    print('=== Cadastro de Cliente ===')
    name = input('Digite o nome do cliente: ')
    cpf = input('Digite o CPF do cliente: ')
    if cpf in [i['CPF'] for i in customers]:
        print('CPF já cadastrado.')
        return
    customers.append({'Nome': name, 'CPF': cpf})
    print('Cliente cadastrado com sucesso!')

def account():
    global accounts
    global account_number
    print('=== Cadastro de Conta ===')
    cpf = input('Digite o CPF do cliente: ')
    if cpf not in [i['CPF'] for i in customers]:
        print('CPF não encontrado.')
        return
    accounts.append({'CPF': cpf, 'Conta': account_number, 'Saques': 3, 'Saldo': 0})
    print('Conta cadastrada com sucesso!')
    print('Número da conta: {:0>4}'.format(account_number))
    account_number += 1

def list_accounts():
    global customers
    global accounts
    print('=== Lista de Clientes ===')
    for i in customers:
        print('Nome: {} | CPF: {}'.format(i['Nome'], i['CPF']))
    print('=== Lista de Contas ===')
    for i in accounts:
        print('CPF: {} | Conta: {:0>4}'.format(i['CPF'], i['Conta']))

def clear_screen():
    # Função para limpar a tela do terminal
    print('\033[H\033[J')

# Menu principal
while True:
    clear_screen()
    print('=== Banco ===')
    print('1. Depósitar')
    print('2. Sacar')
    print('3. Extrato')
    print('4. Criar usuário')
    print('5. Criar conta')
    print('6. Listar usuários e contas')
    print('0. Sair')

    option = input('Escolha uma opção: ')

    if option == '1':
        deposit()
    elif option == '2':
        debit()
    elif option == '3':
        statements()
    elif option == '4':
        client()
    elif option == '5':
        account()
    elif option == '6':
        list_accounts()
    elif option == '0':
        break
    else:
        print('Opção inválida. Escolha uma opção válida.')

    input('Pressione Enter para continuar...')

print('Obrigado por utilizar o nosso Banco!')
