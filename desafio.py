from datetime import datetime  # Importa o módulo para trabalhar com datas e horários

menu = """
######## CAIXA ELETRÔNICO ########
Escolha uma das opções:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

------------------------
=> """

# Variáveis iniciais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)  # Mostra o menu e captura a opção do usuário

    if opcao == "d":
        deposito = float(input("Informe o valor a ser depositado: "))  # Entrada de valor para depósito
        if deposito > 0:  # Verifica se o valor é positivo
            saldo += deposito  # Atualiza o saldo
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Captura data e hora atual
            extrato += f"[{data_hora}] Depósito: R${deposito:.2f}\n"  # Registra operação no extrato
            print(f"O valor de R${deposito:.2f} foi depositado com sucesso!")
        else:
            print("Valor inválido! Favor inserir um valor acima de R$0.")

    elif opcao == "s":
        saque = float(input("Informe o valor a ser sacado: "))  # Entrada de valor para saque

        # Verificações de limite, saldo e número de saques
        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif saque > 0:
            saldo -= saque  # Atualiza o saldo
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Captura data e hora atual
            extrato += f"[{data_hora}] Saque: R${saque:.2f}\n"  # Registra operação no extrato
            numero_saques += 1  # Incrementa o contador de saques
            print(f"O valor de R${saque:.2f} foi sacado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        # Exibe o extrato ou uma mensagem se não houver movimentações
        print("\n################ EXTRATO ################")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("###########################################")

    elif opcao == "q":
        break  # Encerra o loop e o programa

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")  # Opção inválida
