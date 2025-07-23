# Sistema bancário simples com as operações: depósito, saque, extrato e saída

menu = """
================ MENU ===================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=========================================
=> """

# Variáveis principais do sistema
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).strip().lower()

    if opcao == "d":
        # DEPÓSITO
        try:
            valor = float(input("🔹 Informe o valor do depósito: R$ "))
            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito:\t+R$ {valor:.2f}")
                print("✅ Depósito realizado com sucesso!\n")
            else:
                print("❌ Valor inválido. Digite um valor positivo.\n")
        except ValueError:
            print("❌ Entrada inválida. Digite um número.\n")

    elif opcao == "s":
        # SAQUE
        try:
            valor = float(input("🔸 Informe o valor do saque: R$ "))

            if valor <= 0:
                print("❌ Valor inválido. Digite um valor positivo.\n")
                continue

            if valor > saldo:
                print("❌ Operação falhou! Saldo insuficiente.\n")
            elif valor > limite:
                print(f"❌ Limite de saque excedido! Máximo: R$ {limite:.2f}\n")
            elif numero_saques >= LIMITE_SAQUES:
                print("❌ Número máximo de saques diários atingido.\n")
            else:
                saldo -= valor
                extrato.append(f"Saque:\t\t-R$ {valor:.2f}")
                numero_saques += 1
                print("✅ Saque realizado com sucesso!\n")

        except ValueError:
            print("❌ Entrada inválida. Digite um número.\n")

    elif opcao == "e":
        # EXTRATO
        print("\n=========== 📄 EXTRATO ===========")
        print("\n".join(extrato) if extrato else "Nenhuma movimentação registrada.")
        print(f"\nSaldo atual:\tR$ {saldo:.2f}")
        print("==================================\n")

    elif opcao == "q":
        # SAIR
        print("\n🛑 Encerrando o sistema. Até mais!")
        break

    else:
        print("⚠️ Opção inválida. Tente novamente.\n")
