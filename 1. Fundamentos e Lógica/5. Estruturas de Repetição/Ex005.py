# Exercício 1: Imprime os números de 1 a 10 usando um loop for
for i in range(1, 11):
    print(i)


# Exercício 2: Soma todos os números pares de 0 a 100 usando while
soma = 0
num = 0

while num <= 100:
    if num % 2 == 0:
        soma += num
    num += 1

print("Soma dos pares:", soma)


# Exercício 3: Loop infinito que pede senha até digitar corretamente (usando break)
while True:
    senha = input("Digite a senha: ")
    if senha == "admin123":
        print("Senha correta. Saindo...")
        break
    else:
        print("Senha incorreta. Tente novamente.")
