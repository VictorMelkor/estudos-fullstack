# Exercício 1: Verificar o tamanho de diferentes objetos com len()
texto = "Python"
lista = [1, 2, 3, 4]
dicionario = {"a": 1, "b": 2}

print(len(texto))       # 6
print(len(lista))       # 4
print(len(dicionario))  # 2


# Exercício 2: Usar range() para imprimir números de 0 a 4 e de 1 a 9 pulando de 2 em 2
for i in range(5):
    print(i)

for i in range(1, 10, 2):
    print(i)


# Exercício 3: Usar enumerate() para imprimir índices e valores de uma lista
letras = ['x', 'y', 'z']

for i, letra in enumerate(letras):
    print(i, letra)


# Exercício 4: Usar zip() para juntar duas listas e imprimir pares
nomes = ['Ana', 'Bruno']
idades = [25, 30]

for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")


# Exercício 5: Explorar comportamento de tipos em conversões e booleanos
print(bool([]))          # False, lista vazia é falsa
print(bool([0]))         # True, lista com elemento é verdadeira
print(int("10"))         # 10, converte string para inteiro
print(str(123))          # '123', converte número para string
print(float("3.14"))     # 3.14, converte string para float
print(bool(0))           # False
print(bool(1))           # True
