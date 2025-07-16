# Exercício 1: Função recursiva que calcula o fatorial de um número
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

print(fatorial(5))  # Saída: 120


# Exercício 2: Função recursiva que soma todos os elementos de uma lista
def soma_lista(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + soma_lista(lista[1:])

print(soma_lista([1, 2, 3, 4]))  # Saída: 10


# Exercício 3: Função recursiva que calcula o n-ésimo número da sequência de Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i))
