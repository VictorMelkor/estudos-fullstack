####################################
# Módulo Datetime
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
# Time

from datetime import time # apenas hora

hora = time(10, 20, 0)
print(hora) # 10:20:00