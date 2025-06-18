""" # TODO - atividade: Crie um programa que mostre a hora atual sempre sendo atualizada a cada segundo.
# NOTE - para interromper o programa, use a tecla de atalho Ctrl+C"""

import datetime
import time
import os

hora_atual = datetime.datetime.now().strftime("%H:%M:%S")

while True:
    print(f"A hora atual é: {hora_atual}! Para encerrar, pressione Ctrl+C.")
    try: 
        if datetime.datetime.now().strftime("%H:%M:%S") != hora_atual:
            hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")    
        continue 
    except KeyboardInterrupt:
        print("Programa encerrado, como solicitado.")
    break