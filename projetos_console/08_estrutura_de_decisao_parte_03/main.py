#declaração de variáveis
aluno = input("Digite o nome do aluno: ")
media = float(input("Digite a nota média do aluno: ").replace(",", "."))

#estrutura de decisão
if media >= 0 and media <= 10:
    if media >= 7:
        print(f"{aluno} está aprovado.")
    elif media >= 5:
        print(f"{aluno} está em recuperação.")
    else:
        print(f"{aluno} está reprovado.")
else:
    print(f"Nota Inválida!")