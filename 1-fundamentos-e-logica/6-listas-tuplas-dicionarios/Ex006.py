# Exercício 1: Cria uma lista de compras onde o usuário insere 3 itens usando append()
compras = []

for i in range(3):
    item = input("Digite um item para a lista de compras: ")
    compras.append(item)

print("Sua lista de compras:")
for item in compras:
    print("-", item)


# Exercício 2: Usa um dicionário para armazenar nomes como chaves e idades como valores, e exibe os pares
pessoas = {
    "Ana": 30,
    "Bruno": 25,
    "Carla": 22
}

for nome, idade in pessoas.items():
    print(f"{nome} tem {idade} anos")


# Exercício 3: Armazena os dias da semana em uma tupla e imprime cada um em uma nova linha
dias = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")

for dia in dias:
    print(dia)
