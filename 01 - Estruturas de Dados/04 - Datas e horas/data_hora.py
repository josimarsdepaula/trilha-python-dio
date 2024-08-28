from datetime import date
from datetime import datetime

# Cria uma data específica
data = date(2023, 7, 10)
print(data)

# Obtém a data atual
data_hoje = date.today()
print(data_hoje)

# Cria um objeto datetime com data e hora específicas
data_hora = datetime(2023, 7, 23)
print(data_hora)

data_hora2 = datetime.today()
print(data_hora2)
