#declaração de variáveis
nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))
altura = float(input("Qual é a sua altura? ").replace(",", "."))


#estrutura de decisão
if idade >=12 and altura >= 1.15:
    print(f"{nome}, está autorizado a entrar no parque!")
else:   
    print(f"{nome}, não está autorizado a entrar no parque!")    