# Exercício 1: Verifica se o número é positivo, negativo ou zero
numero = float(input("Digite um número: "))

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Zero")


# Exercício 2: Verifica se a senha digitada é igual a "admin123"
senha = input("Digite a senha: ")

if senha == "admin123":
    print("Acesso permitido")
else:
    print("Senha incorreta")


# Exercício 3: Verifica se o ano é bissexto usando regras encadeadas
ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("Ano bissexto")
        else:
            print("Não é bissexto")
    else:
        print("Ano bissexto")
else:
    print("Não é bissexto")
