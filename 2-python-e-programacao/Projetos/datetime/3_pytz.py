# pip install pytz

import datetime
import pytz

# criando datetime com timezone
data = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
print(data) # 2025-07-29 13:12:39.930392-03:00 (data, hora, timezone UTC)


from datetime import datetime

data = datetime.now(pytz.timezone("Europe/Oslo"))
print(data) # 2025-07-29 18:15:05.907793+02:00 (data, hora, timezone UTC)

###########################################
# Trabalhando timezone sem bibliotecas externas

import datetime

# criando datetime com timezone (UTC-3)
data = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3), "BRT"))
print(data) # 2025-07-29 13:19:18.150968-03:00 

# convertendo para outro timezone (UTC)
data_utc = data.astimezone(datetime.timezone.utc)
print(data_utc) # 2025-07-29 16:19:58.668604+00:00