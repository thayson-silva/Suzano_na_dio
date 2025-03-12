import os

saldo = 0
limite = 500
numero_saques = 0
saque_diario = 0
LIMITE_SAQUES = 3
extrato = ""


def desenha_extrato():
    global extrato, saldo
    os.system('cls')

    print("Extrato Bancario".center(50, "-"))
    print()
    print(extrato)
    print()
    print(f"Saldo R${saldo:.2f}".center(50))
    print()
    print("desafio bancario. v1.0".center(50, "-"))
    print()

    os.system('pause')

def desenha_menu():
    menu = '''
        Systema Bancario 

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] sair

        Digite a opção desejada: '''
    
    os.system('cls')
    return input(menu)

def mensagem_systema(mensagem):
    os.system('cls')
    print(mensagem)
    print()
    os.system('pause')

def valor(mensagem):
    os.system('cls')
    
    try:
        return float(input(mensagem))
    except ValueError:
        return 0

while True:
    op = desenha_menu()
    
    if op.lower() == 'd':
        valor_deposito = valor("Informe o valor do depósito: R$")

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito:                          R${valor_deposito:.2f}\n"
            mensagem_systema(f"Depósito no valor de R${valor_deposito:.2f} realizado com sucesso!!")
        else:
            mensagem_systema("Falha na operação, valor informado é inválido")

    elif op.lower() == 's':
        valor_saque = valor("Digite o valor do saque: R$")

        if valor_saque > 0:
            if saldo >= valor_saque:
                if (valor_saque + saque_diario) <= limite:
                    saque_diario += valor_saque
                    if numero_saques < LIMITE_SAQUES:
                        numero_saques += 1
                        saldo -= valor_saque
                        extrato += f"Saque:                             R${valor_saque:.2f}\n"
                        mensagem_systema(f"Saque de R${valor_saque:.2f} realizado com sucesso!")
                    else:
                        mensagem_systema("limite excedido, você só pode realizar 3 saques por dia!")
                else:
                    mensagem_systema("limite diário é de R$500,00!")
            else:
                mensagem_systema("Não foi possivel realizar o saque por falta de saldo!")
        else:
            mensagem_systema("Falha na operação, valor informado é inválido")

    elif op.lower() == 'e':

        if extrato:
            desenha_extrato()
        else:
            mensagem_systema("Não foram realizadas movimentações.")

    elif op.lower() == 'q':
        break
    
    else:
        mensagem_systema("opção inválida!!")
        # os.system('cls')
        # print("opção inválida!!")
        # print()

        # os.system('pause')
        