# 🧠 EXERCÍCIO DE LÓGICA: Censo dos Desenvolvedores

# Você está ajudando a organizar um CENSO DE DESENVOLVEDORES.
# Dado um conjunto de respostas com o nome do dev e as tecnologias que ele usa,
# crie um programa que:
# 1. Conte quantos devs usam cada tecnologia
# 2. Mostre um ranking decrescente de tecnologias mais populares


# 🎯 ENTRADA SIMULADA
respostas = [
    {"nome": "Alice", "tecnologias": ["Python", "JavaScript"]},
    {"nome": "Bob", "tecnologias": ["Python", "C#"]},
    {"nome": "Carol", "tecnologias": ["JavaScript", "HTML", "CSS"]},
    {"nome": "David", "tecnologias": ["Python", "HTML"]},
    {"nome": "Eve", "tecnologias": ["C#", "JavaScript"]},
]

# 🔢 Criamos um dicionário para contar quantos devs usam cada tecnologia
contagem = {}

# 🔄 Iteramos por cada resposta da lista
for resposta in respostas:
    for tecnologia in resposta["tecnologias"]:
        # Se a tecnologia já está no dicionário, incrementa
        if tecnologia in contagem:
            contagem[tecnologia] += 1
        # Senão, adiciona com valor 1
        else:
            contagem[tecnologia] = 1

# 🧮 Agora transformamos o dicionário em lista de tuplas e ordenamos por quantidade
ranking = sorted(contagem.items(), key=lambda item: item[1], reverse=True)

# 📊 Exibimos o resultado final
print("Ranking de tecnologias mais populares:")
for i, (tecnologia, quantidade) in enumerate(ranking, start=1):
    print(f"{i}. {tecnologia} - {quantidade} devs")


# 🧠 CONCEITOS APLICADOS:
# - Dicionários (dict): usados para contar ocorrências de cada tecnologia
# - Laços for: percorrem listas e listas aninhadas
# - Condicional if/else: verifica se a tecnologia já foi contada
# - Função sorted: ordena as tuplas com base no valor (quantidade de devs)
# - Função enumerate: gera índices para o ranking (começando do 1)
# - F-strings: usadas para imprimir resultados formatados

# 💡 EXPANSÕES POSSÍVEIS:
# - Receber dados via input do usuário (em vez de lista fixa)
# - Armazenar ou ler dados em JSON
# - Exibir os dados em gráfico com matplotlib
# - Separar frontend/backend e criar interface com tkinter ou HTML
