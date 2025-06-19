import datetime
from datetime import date

hoje = date.today().strftime("%d/%m/%Y")
hora = datetime.datetime.now().strftime("%H:%M:%S")

print(f"Data de hoje: {hoje}.")
print(f"A hora de da execução: {hora}.")