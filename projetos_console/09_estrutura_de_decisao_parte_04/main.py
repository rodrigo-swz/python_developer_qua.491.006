#declaração de variáveis
nome = input("Informe o seu nome: ")
idade = int(input("Informe a sua idade: "))

#ternario
result = "é maior de idade." if idade >= 18 else "é menor de idade."

#saída
print(f"{nome} {result}")