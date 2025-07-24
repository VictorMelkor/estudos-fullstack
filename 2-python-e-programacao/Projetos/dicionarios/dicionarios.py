# São conjuntos não ordenados de pares chave:valor.
# chaves são únicas em uma dada instância do dicionário (valores imutaveis)

pessoa = {"nome": "Guilherme", "idade": 28} # {chave: valor}

pessoa = dict(nome="Guilherme", idade=28) # declara usando a classe construtora dict

pessoa["telefone"] = "3333-1234" # {"Nome": "Guilhemre", "idade": 28, "telefone": "3333-1234"} #adiciona chave e valor em um dict já existente

# pode ser feita assim:
# pessoa = {
#     "nome": "Guilherme", 
#     "idade": 28
#     }

dados = {"nome": "Guilhemre", "idade": 28, "telefone": "3333-1234"}

dados["nome"] # Guilherme
dados["idade"] # 28
dados["telefone"] # 3333-1234

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

dados # {"nome": "Maria", "idade": 28, "telefone": "9988-1781"}



#########################################
# Dicionários aninhados

contatos = {
    'guilherme@gmail.com': {"Nome": "Guilhemre", "idade": 28, "telefone": "3333-1234"},
    'maria@gmail.com': {"nome": "Maria", "idade": 28, "telefone": "9988-1781"},
    "chappie@gmail.com": {"nome": "Chappie", "idade": 18, "telefone": "1234-1234"},
    "melanie@gmail.com": {"nome": "Melanie", "idade": 37, "telefone": "4512-2154", "extra": {"b": 1}} #um dicionário, dentro de um dicionário, dentro de outro dicionário
} 

contatos["melanie@gmail.com"] # {"nome": "Melanie", "idade": 37, "telefone": "4512-2154"}
contatos["melanie@gmail.com"]["telefone"] # "4512-2154"

telefone = contatos["melanie@gmail.com"]["telefone"] # "4512-2154"
print(telefone)

extra = contatos["melanie@gmail.com"]["extra"]["b"] #acessando o dicionário dentro de outro dicionário
print(extra)


#################################################
# Iteraçções

for chave in contatos:
    print(chave, contatos[chave]) # não é a melhor forma de iterar

print("---------------------------")

for chave, valor in contatos.items(): # os resultados são iguais, mas o método é mais elegante
    print(chave, valor)