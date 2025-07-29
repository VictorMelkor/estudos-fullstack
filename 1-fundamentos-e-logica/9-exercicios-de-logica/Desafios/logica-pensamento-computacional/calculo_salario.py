# Para ler e escrever dados em Python, usamos as seguintes funções:
# input: lê UMA linha com dado(s) de entrada do usuário;
# print: imprime um texto de Saída (output), pulando linha;

# função útil para o calculo do imposto (baseado nas aliquotas):
def calcular_imposto(salario):
    aliquota = 0.0
    if (salario >= 0 and salario <= 1100):
        aliquota = 0.5
    elif (salario >= 1100.1 and salario <= 2500):
        aliquota = 0.10
    else:
        aliquota = 0.15
    
    return aliquota * salario

# Lê os valores de Entrada
valor_salario = float(input())
valor_beneficio = float(input())

#Calcula o imposto através da função calcular_imposto:
valor_imposto = calcular_imposto(valor_salario)
# Calcula e imprime a Saída (com 2 casas decimais):
saida = valor_salario - valor_imposto + valor_beneficio
print(f'{saida:.2f}')