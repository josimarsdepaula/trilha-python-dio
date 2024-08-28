import textwrap


def menu():
    menu_options = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_options))


def depositar(saldo, valor, extrato):
    if valor <= 0:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return saldo, extrato

    saldo += valor
    extrato += f"Depósito:\tR$ {valor:.2f}\n"
    print("\n=== Depósito realizado com sucesso! ===")
    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return saldo, extrato, numero_saques

    if valor > saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif valor > limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif numero_saques >= limite_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    else:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if cpf in usuarios:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios[cpf] = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }
    print("=== Usuário criado com sucesso! ===")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = usuarios.get(cpf)
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario,
            "saldo": 0,
            "extrato": "",
            "numero_saques": 0
        }

    print("\n@@@ Usuário não encontrado. Conta não criada. @@@")
    return None


def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    for conta in contas.values():
        print("=" * 100)
        print(f"Agência:\t{conta['agencia']}")
        print(f"C/C:\t\t{conta['numero_conta']}")
        print(f"Titular:\t{conta['usuario']['nome']}")
        print("=" * 100)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = {}
    contas = {}

    while True:
        opcao = menu()

        if opcao == "d":
            numero_conta = input("Digite o número da conta: ")
            conta = contas.get(numero_conta)
            if conta:
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = depositar(conta['saldo'], valor, conta['extrato'])
                conta['saldo'] = saldo
                conta['extrato'] = extrato
                contas[numero_conta] = conta
            else:
                print("Conta não encontrada.")

        elif opcao == "s":
            numero_conta = input("Digite o número da conta: ")
            conta = contas.get(numero_conta)
            if conta:
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato, numero_saques = sacar(
                    conta['saldo'], valor, conta['extrato'], limite, conta['numero_saques'], LIMITE_SAQUES
                )
                conta['saldo'] = saldo
                conta['extrato'] = extrato
                conta['numero_saques'] = numero_saques
                contas[numero_conta] = conta
            else:
                print("Conta não encontrada.")

        elif opcao == "e":
            numero_conta = input("Digite o número da conta: ")
            conta = contas.get(numero_conta)
            if conta:
                exibir_extrato(conta['saldo'], conta['extrato'])
            else:
                print("Conta não encontrada.")

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = str(len(contas) + 1)
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas[numero_conta] = conta

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
