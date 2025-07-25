## Métodos em dicionários

contatos = {
    'guilherme@gmail.com': {"Nome": "Guilhemre", "idade": 28, "telefone": "3333-1234"},
    'maria@gmail.com': {"nome": "Maria", "idade": 28, "telefone": "9988-1781"},
    "chappie@gmail.com": {"nome": "Chappie", "idade": 18, "telefone": "1234-1234"},
    "melanie@gmail.com": {"nome": "Melanie", "idade": 37, "telefone": "4512-2154"},
    } 

##########################
# .clear # Limpa completamente o dicionário

contatos.clear() 
contatos # {}

##########################
# .copy # copia o conteudo do dicionário

contatos = {
    'guilherme@gmail.com': {"Nome": "Guilhemre", "idade": 28, "telefone": "3333-1234"}
}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"} #sobrescreve o conteudo do dicionário

contatos["guilherme@gmail.com"] # {"nome": "Guilherme", "telefone": "3333-1234"}
copia["guilherme@gmail.com"] # {"nome": "Gui"}

##########################
# .fromkeys # cria chaves no dicionário
# pode ser um dicionário existente ou um novo dicionário

dict.fromkeys(["nome", "telefone"]) # {"nome": None, "telefon": None} ## cria chaves com valor None

dict.fromkeys(["nome", "telefone"], "vazio") # {"nome": "vazio", "telefone": "vazio"} ## Cria chaves com valor informado

##########################
# .get # busca o valor da chave buscada ou retorna None se ela não existe

contatos = {
    'guilherme@gmail.com': {"Nome": "Guilhemre", "idade": 28, "telefone": "3333-1234"}
}

contatos["chave"] # KeyError ## chave inexistente retorna erro

contatos.get("chave") # None ## chave inexistente retorna None
contatos.get("chave", {}) # {} ## chave inexistente retorna um dict vazio
contatos.get("guilherme@gmail.com", {}) # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"}} ## chave existente, retorna a chave


##########################
# .item # usado para iterar o dicionário, com for por exemplo
## retorna uma lista com os itens

contatos = {
    'guilherme@gmail.com': {"Nome": "Guilhemre", "idade": 28, "telefone": "3333-1234"}
}

contatos.items() # dict_items([('guilhemer@gmail.com, {"nome": "Guilherme", "telefone": "3333-1234"})])


##########################
# .keys # retorna as chaves do dicionário

contatos = {
    'guilherme@gmail.com': {"Nome": "Guilhemre", "idade": 28, "telefone": "3333-1234"}
}

contatos.keys() # dict_keys(['guiherme@gmail.com])

novo_dicionario = {"a": 1, 1: "teste", "b": "python"}
novo_dicionario.keys() # dict_keys(["a", 1, "b"])

##########################
# .pop # remove um par chave e valor do dicionário a partir da chave indicada no comando

contatos = {
    'guilherme@gmail.com': {"Nome": "Guilhemre", "idade": 28, "telefone": "3333-1234"}
}

contatos.pop("guilherme@gmail.com") #{"nome": "Guilherme", "telefone": "3333-1234"}  # mostra o que vai ser removido conforme a chave informada
contatos.pop("guilherme@gmail.com", {}) # {} # retorna um dict vazio caso não encontre a chave buscada

##########################
# .setdefautl # serve para adicionar valores caso não existam no dict sem necessidade de verificar todas as chaves:valores

contatos = {
    'guilherme@gmail.com': {"Nome": "Guilhemre", "idade": 28, "telefone": "3333-1234"}
}

contatos.setdefault("nome", "Giovanna") # Guilherme ## se o atributo indicado  existe no dicionário, retorna o valor existente para o atributo
contatos # {"nome": "Guilherme", "telefone": "3333-1234"}

contatos.setdefault("idade", 28) # 28 ## se o atributo indicado não existir, ele adiciona o atributo e valor
contatos # {"nome": "Guilherme", "telefone": "3333-1234", "idade": 28}

##########################
# .update # serve para atualizar o dicionário com outro dicionário

contatos = {
    'guilherme@gmail.com': {"Nome": "Guilhemre", "idade": 28, "telefone": "3333-1234"}
}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}}) # sobrescreve os valores do dicionario se a chave já existe
contatos # {"guilherme@gmail.com": {"nome": "Gui"}}

contatos.update({"giovana@gmail.com": {"nome": "Giovana", "telefone": "3322-8181"}}) # adiciona os valores se a chave não existir
contatos # {"guilherme.com": {"nome": "Gui"}, "giovana@gmail.com": {"nome": Giovana}, "telefone": "3322-8181"}


##########################
# .values # retorna os valores, da mesmo forma que .keys retorna as chaves

contatos = {
    'guilherme@gmail.com': {"Nome": "Guilhemre", "idade": 28, "telefone": "3333-1234"},
    'maria@gmail.com': {"nome": "Maria", "idade": 28, "telefone": "9988-1781"},
    "chappie@gmail.com": {"nome": "Chappie", "idade": 18, "telefone": "1234-1234"},
    "melanie@gmail.com": {"nome": "Melanie", "idade": 37, "telefone": "4512-2154"},
    } 

##########################
# .in # retorna booleano se o valor solicitado existe no dicionário

contatos = {
    'guilherme@gmail.com': {"Nome": "Guilhemre", "idade": 28, "telefone": "3333-1234"},
    'maria@gmail.com': {"nome": "Maria", "idade": 28, "telefone": "9988-1781"},
    "chappie@gmail.com": {"nome": "Chappie", "idade": 18, "telefone": "1234-1234"},
    "melanie@gmail.com": {"nome": "Melanie", "idade": 37, "telefone": "4512-2154"},
    } 

"guilherme@gmail.com" in contatos # True
"@megui@gmail.com" in contatos # False
"idade" in ["guilherme@gmail.com"] # False


##########################
# .del # remove o objeto passado

contatos = {
    'guilherme@gmail.com': {"Nome": "Guilhemre", "idade": 28, "telefone": "3333-1234"},
    'maria@gmail.com': {"nome": "Maria", "idade": 28, "telefone": "9988-1781"},
    "chappie@gmail.com": {"nome": "Chappie", "idade": 18, "telefone": "1234-1234"},
    "melanie@gmail.com": {"nome": "Melanie", "idade": 37, "telefone": "4512-2154"},
    } 

del contatos["guilherme@gmail.com"]["telefone"] #remove telefone dentro do dicionário guilherme@gmail.com
del contatos["chappie@gmail.com"] # remove todo o dicionário com esse valor

contatos # {'guilherme@gmail.com': {"Nome": "Guilhemre", "idade": 28}, 'maria@gmail.com': {"nome": "Maria", "idade": 28, "telefone": "9988-1781"}, "melanie@gmail.com": {"nome": "Melanie", "idade": 37, "telefone": "4512-2154"}} 