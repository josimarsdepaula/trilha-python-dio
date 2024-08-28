from datetime import datetime, timedelta

tipo_de_carro = """
######## Automóvel ########
Escolha um tipo de carro:

[P] Pequeno
[M] Médio
[G] Grande

------------------------
=> """

tipo_carro = input(tipo_de_carro)

tempo_pequeno = 30
tempo_medio = 60
tempo_grande = 90
data_atual = datetime.now()

if tipo_carro.upper() == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"Você escolheu um carro Pequeno.")
    print(f"O Carro chegou: {data_atual.strftime('%d/%m/%Y %H:%M:%S')} e ficará pronto às {data_estimada.strftime('%d/%m/%Y %H:%M:%S')}")

elif tipo_carro.upper() == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"Você escolheu um carro Médio.")
    print(f"O Carro chegou: {data_atual.strftime('%d/%m/%Y %H:%M:%S')} e ficará pronto às {data_estimada.strftime('%d/%m/%Y %H:%M:%S')}")

elif tipo_carro.upper() == 'G':
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"Você escolheu um carro Grande.")
    print(f"O Carro chegou: {data_atual.strftime('%d/%m/%Y %H:%M:%S')} e ficará pronto às {data_estimada.strftime('%d/%m/%Y %H:%M:%S')}")

else:
    print("Opção inválida! Por favor, escolha P, M ou G.")
