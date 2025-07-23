# Exercício 1: Define uma função que recebe um nome como parâmetro e exibe uma saudação personalizada
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Victor")


# Exercício 2: Define uma função que verifica se o número recebido é par ou ímpar e retorna uma string correspondente
def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

print(par_ou_impar(7))  # Saída: ímpar


# Exercício 3: Define uma função que calcula o fatorial de um número usando um loop for
def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(fatorial(5))  # Saída: 120
