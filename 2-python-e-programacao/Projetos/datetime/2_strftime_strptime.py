#####################################
# Conversão e Formatação de Datas e Horas com strftime e strptime

#####################################
# strf = formatação

import datetime

data = datetime.datetime.now()

# formatando data e hora
print(data.strftime("%d/%m/%Y %H:%M")) # 29/07/2025 12:48


#####################################
# strp = parse

# Convertendo string para datetime
data_string = "30/07/2025 15:30"
data = datetime.datetime.strptime(data_string, "%d/%m/%Y %H:%M") # parse com strptime
print(data) # 2025-07-30 15:30:00
print(data.strftime("%d/%m/%Y %H:%M")) #30/07/2025 15:30:00 # formatação com strftime

#####################################
# Aplicação strftime

from datetime import datetime

data_hora_atual = datetime.now()
data_hora_string = "2025-07-29 10:20"
mascara_ptbr = "%d/%m/%Y %a" # a máscara suprime horas e minutos dessa forma # %a apresenta o dia da semana em ingles
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

#####################################
# Aplicação strptime

data_convertida = datetime.strptime(data_hora_string, mascara_en) # faz parse de data_hora_string com formato da mascara_en
print(data_convertida)
print(type(data_convertida)) # <class 'datetime.datetime'>

