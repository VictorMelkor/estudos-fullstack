# Exercício 1: Criação de variáveis com diferentes tipos (string, int, float)
nome = "Victor"
idade = 30
saldo = 100.50


# Exercício 2: Soma entre float e int, e verificação do tipo resultante
resultado = saldo + 10
print(resultado)            # Saída: 110.5
print(type(resultado))      # Saída: <class 'float'>


# Exercício 3: Conversão de string para int com tratamento de erro usando try/except
entrada = "abc"

try:
    numero = int(entrada)
    print(numero)
except ValueError:
    print("Erro: não é possível converter para número.")
