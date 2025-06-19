"""
TODO - atividade: Cria um programa que recebe do usuário o nome e a idade, 
e em seguida motra um menu de filmes com suas respectivas classificações indicativas e salas de exibição.
 Exemplo:
- Sala 1: A roda quadrada - Livre
- Sala 2: A volta dos que não foram - 12 anos
O usuário deve escolher a sala que está passando o filme que deseja assistir.
Se o usuário tiver a idade mínima ou mais para ver o filme, o programa imprime o ingresso com o nome do usuário,
 a sala, o nome do filme, a data e a hora da compra do ingresso, e seje um bomfilme, e em seguida encerra o programa.
 sE O USUÁRIO NÃO TIVER A IDADE MÍNIMA PRA VER O FILME, O PROGRAMA BLOQUEIA A SUA ENTRADA, 
 e re-exibe o menu de filmes para que ele escolha outro filme."""

import datetime
import os
from datetime import date

data = date.today().strftime("%d/%m/%Y")
hora = datetime.datetime.now().strftime("%H:%M:%S")

sala1 = "Toy Story"
sala2 = "O senhor dos anéis"
sala3 = "Vingadores: Ultimato"
sala4 = "Deadpool"
sala5 = "A viagem de Chihiro"

try:
    nome = input("Informe o seu nome:").title().strip()
    idade = int(input('Informe sua idade: '))
    while True:
        print(f"{'-'*20} 🎥🎞️ MENU DE FILMES -- JOW CINE 📽️🎦{'-'*20}\n")
        print("Sala 1 - {sala1}, Classificação LIVRE")
        print("Sala 2 - {sala2}, Classificação 12 anos")
        print("Sala 3 - {sala3}, Classificação LIVRE")
        print("Sala 4 - {sala4}, Classificação 16 anos")
        print("Sala 5 - {sala5}, Classificação 10 anos")
        sala = input("Informe a sala desejada: ").strip()
        os.system("cls" if os.name == 'nt' else "clear")
        match sala:
            case "1":
                idade_minima = 0
                filme = sala1
            case "2":
                idade_minima = 12
                filme = sala2
            case "3":
                idade_minima = 0
                filme = sala3
            case "4":
                idade_minima = 16
                filme = sala4
            case "5":
                idade_minima = 10
                filme = sala5
            case _:
                print("Sala inexistente, favor escolher uma sala válida.")
                continue
        if idade >= idade_minima:
            print(f"{'-'*20} INGRESSO JOW CINE{'-'*20}")
            print(f"{'-'*60}\n")
            print(f"Filme: {filme} - {idade_minima}.")
            print(f"Ingresso comprado por {nome} no dia {data} às {hora}.")
            print(f"TENHA UM ÓTIMO FILME!!!🎥🎞️📽️🎦")
            break
        else:
            print(f"{nome} não possui a idade mínima para ver {filme}")
            print(f"Favor escolher outro filme indicado para sua idade.")
            continue
except Exception as e:
    print(f"Não foi possível comprar ingresso. {e}.")
