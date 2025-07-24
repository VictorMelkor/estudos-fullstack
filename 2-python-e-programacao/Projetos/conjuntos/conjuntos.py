# Set (palavra reservada)
# Não respeita ordem

numeros = set([1, 2, 3, 1, 3, 4]) #{ 1, 2, 3, 4}

abacaxi = set("abacaxi") # {"b", "a", "c", "x", "i"} 

carros = set(("palio", "gol", "celta", "palio", "onix")) # {"gol", "celta", "palio"}

print("set números")
print(numeros)
print("---------------")

print("set abacaxi")
print(abacaxi)
print("---------------")

print("set carros")
print(carros)
print("---------------")

linguagens = {"python", "java", "python"}

print("linguagens")
print(linguagens)
print("---------------")

#####################

numeros = list(numeros) #Pra consumir os valores, é preciso transformar em lista
print("numeros em lista, na posição [0]")
print(numeros[0])

print("set carros iterado com for")
for carro in carros: # é possivel iterar em estruturas de repetição
    print(carro)
print("---------------")

print("set carros iterado com for e indice, usando enumerate")
for indice, carro in enumerate(carros): # a ordem permanece aleatória
    print(f"{indice}: {carro}")
print("---------------")


#####################
# .union # une o conteúdo dos conjuntos

conjunto_a = {1 ,2}
conjunto_b = {3, 4}

print("conjunto a")
print(conjunto_a)
print("---------------")
print("conjunto b")
print(conjunto_b)
print("---------------")

conjunto_a.union(conjunto_b) # {1, 2, 3, 4}

print("union de a e b")
print(conjunto_a.union(conjunto_b))
print("---------------")

#####################
# .intersection #  busca os itens que fazem parte dos dois conjuntos

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}


conjunto_a.intersection(conjunto_b) # {2, 3}


print("intersection de a e b")
print(conjunto_a.intersection(conjunto_b))
print("---------------")

#####################
# .difference # busca os itens que não fazem parte do grupo de forma separada

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}

print("difference de a para b")
print(conjunto_a.difference(conjunto_b))
print("---------------")

print("difference de b para a")
print(conjunto_b.difference(conjunto_a))
print("---------------")


#####################
# .symmetric_difference # busca os itens que não fazem parte dos grupos, mas de forma unida

conjunto_a.symmetric_difference(conjunto_b) # {1, 4}

print(".symmetric_difference de a e b")
print(conjunto_a.symmetric_difference(conjunto_b))
print("---------------")

#####################
# .issubset # retorna booleano se um conjunto é subconjunto de outro

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b) # True
conjunto_b.issubset(conjunto_a) # False

#####################
# .issuperset # retorna booleano se um conjunto conter outro conjunto

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issuperset(conjunto_b) # False
conjunto_b.issuperset(conjunto_a) # True

######################
# .isdisjoint # retorna booleano informando se os conjuntos NÃO se tocam, ou seja, não tem itens que se repetem em cada conjunto

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b) # True (retorna True pois NÃO tem itens iguais )
conjunto_a.isdisjoint(conjunto_c) # False (retorna False pois TEM itens iguais)


#######################
# .add # adiciona itens ao set que ainda não existam

sorteio = {1, 23}

sorteio.add(25) # {1, 23, 25}
sorteio.add(42) # {1, 23, 25, 42}
sorteio.add(25) # {1, 23, 25, 42} # não adiciona valores repetidos


#########################
# .clear # apaga o conteudo do set

sorteio = {1, 23}

sorteio # {1, 23}
sorteio.clear() 
sorteio # {} 

##########################
# .discard # remove o valor indicado

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1) #remove 1
numeros.discard(45) # não remove o que não faz parte

numeros # {2, 3, 4, 5, 6, 7, 8, 9, 0}


############################
# .pop #

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros #{1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.pop() #1 # vai remover a primeira posição (que no caso é o 1)
numeros.pop() #2 # vai remover novamente a primeira posição, que agora é o 2)
numeros # {{3, 4, 5, 6, 7, 8, 9, 0}}

############################
# .remove # faz o mesmo que o .discard, mas caso seja solicitado a remoção de um valor que não exista no set haverá KeyError
