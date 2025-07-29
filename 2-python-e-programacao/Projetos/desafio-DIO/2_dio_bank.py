# ================== Dados Globais ==================
usuarios = []
contas = []
AGENCIA = "0001"

# ================== Funções ==================
def deposito(saldo, valor, extrato, /):
    """Função de depósito (somente argumentos posicionais)."""
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito:\t+R$ {valor:.2f}")
        print("✅ Depósito realizado com sucesso!\n")
    else:
        print("❌ Valor inválido. Digite um valor positivo.\n")
    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """Função de saque (somente argumentos nomeados)."""
    if valor <= 0:
        print("❌ Valor inválido. Digite um valor positivo.\n")
    elif valor > saldo:
        print("❌ Operação falhou! Saldo insuficiente.\n")
    elif valor > limite:
        print(f"❌ Limite de saque excedido! Máximo: R$ {limite:.2f}\n")
    elif numero_saques >= limite_saques:
        print("❌ Número máximo de saques diários atingido.\n")
    else:
        saldo -= valor
        extrato.append(f"Saque:\t\t-R$ {valor:.2f}")
        numero_saques += 1
        print("✅ Saque realizado com sucesso!\n")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    """Função de extrato (posicional e nomeado)."""
    print("\n=========== 📄 EXTRATO ===========")
    print("\n".join(extrato) if extrato else "Nenhuma movimentação registrada.")
    print(f"\nSaldo atual:\tR$ {saldo:.2f}")
    print("==================================\n")


def criar_usuario():
    """Cadastra um novo usuário no sistema."""
    cpf = input("Informe o CPF (somente números): ").strip()

    # Verifica se já existe usuário com esse CPF
    usuario = filtrar_usuario(cpf)
    if usuario:
        print("❌ Já existe um usuário com esse CPF!\n")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("✅ Usuário criado com sucesso!\n")


def filtrar_usuario(cpf):
    """Retorna o usuário com o CPF informado ou None."""
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_conta():
    """Cria uma nova conta vinculada a um usuário existente."""
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = filtrar_usuario(cpf)

    if usuario:
        numero_conta = len(contas) + 1
        contas.append({"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario})
        print(f"✅ Conta criada com sucesso! Agência: {AGENCIA}, Conta: {numero_conta}\n")
    else:
        print("❌ Usuário não encontrado. Cadastre o usuário antes.\n")


def listar_contas():
    """Lista todas as contas cadastradas."""
    for conta in contas:
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}")
    print()


# ================== Programa Principal ==================
menu = """
================ MENU ===================
[d] Depositar
[s] Sacar
[e] Extrato
[u] Novo Usuário
[c] Nova Conta
[l] Listar Contas
[q] Sair
=========================================
=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).strip().lower()

    if opcao == "d":
        try:
            valor = float(input("🔹 Informe o valor do depósito: R$ "))
            saldo, extrato = deposito(saldo, valor, extrato)
        except ValueError:
            print("❌ Entrada inválida. Digite um número.\n")

    elif opcao == "s":
        try:
            valor = float(input("🔸 Informe o valor do saque: R$ "))
            saldo, extrato, numero_saques = saque(
                saldo=saldo, valor=valor, extrato=extrato,
                limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES
            )
        except ValueError:
            print("❌ Entrada inválida. Digite um número.\n")

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "u":
        criar_usuario()

    elif opcao == "c":
        criar_conta()

    elif opcao == "l":
        listar_contas()

    elif opcao == "q":
        print("\n🛑 Encerrando o sistema. Até mais!")
        break

    else:
        print("⚠️ Opção inválida. Tente novamente.\n")
