# matematica.py
# Exercício 1: Crie um módulo com funções matemáticas
# Funções: dobro, triplo e quadrado de um número

def dobro(n):
    return n * 2

def triplo(n):
    return n * 3

def quadrado(n):
    return n ** 2



# operacoes.py
# Exercício 2: Crie uma função que retorna múltiplos valores
# Retorna mínimo, máximo e média de uma lista de números

def estatisticas(lista):
    minimo = min(lista)
    maximo = max(lista)
    media = sum(lista) / len(lista)
    return minimo, maximo, media



# main.py
# Exercício 3: Importe funções de outros arquivos e use-as

from matematica import dobro, triplo
from operacoes import estatisticas

print(dobro(4))        # Saída: 8
print(triplo(2))       # Saída: 6

valores = [10, 20, 30]
print(estatisticas(valores))  # Saída: (10, 30, 20.0)

# Execução condicional para rodar testes isoladamente
if __name__ == "__main__":
    print("Testes rodando no main.py")
    print(dobro(10))  # 20
    print(triplo(5))  # 15
    menor, maior, media = estatisticas([1, 3, 5, 7])
    print(f"Menor: {menor}, Maior: {maior}, Média: {media}")
