# TRATAMENTO DE EXCEÇÃO
try:
    n = int(input("Informe um número: "))
    print(f"O número informado foi: {n}")
except Exception as e:
    print(f"Não foi possível exibir o número. {e}.")
finally:
    print("Programa encerrado com sucesso!")