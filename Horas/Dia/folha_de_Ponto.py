from datetime import datetime

def obter_horario(mensagem):
    while True:
        try:
            horario = input(mensagem + " (formato HH:MM): ")
            datetime.strptime(horario, "%H:%M")
            return horario
        except ValueError:
            print("Formato de hora inválido. Tente novamente.")

def calcular_horas_trabalhadas():
    entrada_manha = obter_horario("Digite o horário de entrada pela manhã")
    saida_almoco = obter_horario("Digite o horário de saída para o almoço")
    entrada_tarde = obter_horario("Digite o horário de entrada após o almoço")
    saida_noite = obter_horario("Digite o horário de saída à noite")

    formato_hora = "%H:%M"

    # Convertendo os horários para objetos datetime
    entrada_manha = datetime.strptime(entrada_manha, formato_hora)
    saida_almoco = datetime.strptime(saida_almoco, formato_hora)
    entrada_tarde = datetime.strptime(entrada_tarde, formato_hora)
    saida_noite = datetime.strptime(saida_noite, formato_hora)

    # Calculando o total de horas trabalhadas
    horas_manha = (saida_almoco - entrada_manha).total_seconds() / 3600
    horas_tarde = (saida_noite - entrada_tarde).total_seconds() / 3600

    total_horas_trabalhadas = horas_manha + horas_tarde

    return total_horas_trabalhadas

# Exemplo de uso
horas_trabalhadas = calcular_horas_trabalhadas()
print(f"Horas trabalhadas no dia: {horas_trabalhadas:.2f} horas")
