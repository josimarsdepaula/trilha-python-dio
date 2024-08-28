from datetime import datetime, timedelta

# Apresento ao usuário as opções de tipo de carro
tipo_de_carro = """
######## Automóvel ########
Escolha um tipo de carro:

[P] Pequeno
[M] Médio
[G] Grande

------------------------
=> """

# Solicito ao usuário que escolha o tipo de carro
tipo_carro = input(tipo_de_carro)

# Defino os tempos estimados para cada tipo de carro em minutos
tempo_pequeno = 30
tempo_medio = 60
tempo_grande = 90

# Capturo a data e hora atuais
data_atual = datetime.now()

# Verifico qual tipo de carro foi escolhido
if tipo_carro.upper() == 'P':
    # Se o carro for Pequeno, calculo a data e hora de conclusão adicionando 30 minutos
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    # Exibo as informações de chegada e o tempo estimado para conclusão
    print(f"Você escolheu um carro Pequeno.")
    print(f"O Carro chegou: {data_atual.strftime('%d/%m/%Y %H:%M:%S')} e ficará pronto às {data_estimada.strftime('%d/%m/%Y %H:%M:%S')}")

elif tipo_carro.upper() == 'M':
    # Se o carro for Médio, calculo a data e hora de conclusão adicionando 60 minutos
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    # Exibo as informações de chegada e o tempo estimado para conclusão
    print(f"Você escolheu um carro Médio.")
    print(f"O Carro chegou: {data_atual.strftime('%d/%m/%Y %H:%M:%S')} e ficará pronto às {data_estimada.strftime('%d/%m/%Y %H:%M:%S')}")

elif tipo_carro.upper() == 'G':
    # Se o carro for Grande, calculo a data e hora de conclusão adicionando 90 minutos
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    # Exibo as informações de chegada e o tempo estimado para conclusão
    print(f"Você escolheu um carro Grande.")
    print(f"O Carro chegou: {data_atual.strftime('%d/%m/%Y %H:%M:%S')} e ficará pronto às {data_estimada.strftime('%d/%m/%Y %H:%M:%S')}")

else:
    # Se o usuário inserir uma opção inválida, exibo uma mensagem de erro
    print("Opção inválida! Por favor, escolha P, M ou G.")
