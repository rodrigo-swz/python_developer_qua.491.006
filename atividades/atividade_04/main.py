""" #  - atividade: Crie um programa que mostre a hora atual sempre sendo atualizada a cada segundo.
# - para interromper o programa, use a tecla de atalho Ctrl+C"""

import datetime
import time
import os

while True:
    hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
    os.system("cls" if os.name == "nt" else "clear")
    print(f"A hora atual é: {hora_atual}! Para encerrar, pressione Ctrl+C.")
    time.sleep(1)
