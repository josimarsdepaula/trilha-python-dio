from datetime import datetime
import pytz

# Obtenho a data e hora atuais na timezone de Oslo, Europa
data = datetime.now(pytz.timezone("Europe/Oslo"))

# Obtenho a data e hora atuais na timezone de São Paulo, Brasil
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

# Imprimo a data e hora de Oslo
print(data)

# Imprimo a data e hora de São Paulo
print(data2)
