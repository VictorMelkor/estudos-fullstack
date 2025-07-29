####################################
# Módulo datetime
# usado para lidar com datas e horas (date, time, timedelta)

####################################
# date
from datetime import date # apenas data

data = date(2025, 7, 29) # (YYYY, MM, DD)
print(data) # 2025-07-29

print(date.today()) # imprime o dia atual


####################################
# datetime

from datetime import datetime # data e horário

data_hora = datetime(2025, 7, 29, 10, 30, 20) # (YYYY, MM, DD, Hora, Minuto, Segundo) # milisegundos omitidos
print(data_hora) # 2025-07-29 10:30:20

data_hora_opcional = datetime(2025, 7, 29) # (YYYY, MM, DD) # zera os atributos opcionais
print(data_hora_opcional) # 2025-07-29 00:00:00 

print(datetime.today()) # imprime dia e hora atual, com milisegundos

####################################
# time

from datetime import time # apenas hora

hora = time(10, 20, 0)
print(hora) # 10:20:00

####################################
# timedelta

from datetime import timedelta # realiza operação de passagem de tempo

# criando data e hora
data = datetime(2025, 7, 29, 13, 45)
print(data) # 2025-07-29 13:45:00

# adicionando uma semana
data = data + timedelta(weeks=1) # passagem de 7 dias
print(data) # 2025-08-07 13:45:00

# Exemplo prático (tempo de lavagem de carro)

tipo_carro = 'M' # P, M, G
tempo_pequeno = 30 # minutos
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now() # trás data com fuso horário

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno) # poderia ser days, weeks, seconds, etc
    print(f'O carro chegou: {data_atual} e ficará `as {data_estimada}')
    pass
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio) # a operação poderia também ser de decreção (-)
    print(f'O carro chegou: {data_atual} e ficará `as {data_estimada}')
    pass
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'O carro chegou: {data_atual} e ficará `as {data_estimada}')
    pass