# Exercício 1: Verifica se a idade permite votar (idade igual ou maior que 16)
idade = int(input("Digite a idade: "))

if idade >= 16:
    print("Pode votar.")
else:
    print("Não pode votar.")


# Exercício 2: Exemplos de expressões lógicas com and, or e not
a = True
b = False
c = True

resultado1 = a and b           # False
resultado2 = a or b            # True
resultado3 = a and b or c      # True (a and b é False, mas c é True)
resultado4 = not a or b        # False (not a = False, b = False)

print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)


# Exercício 3: Calculadora simples com tratamento de erro para divisão por zero
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Escolha a operação (+, -, *, /): ")

if operador == "+":
    print(num1 + num2)
elif operador == "-":
    print(num1 - num2)
elif operador == "*":
    print(num1 * num2)
elif operador == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Erro: divisão por zero.")
else:
    print("Operador inválido.")
