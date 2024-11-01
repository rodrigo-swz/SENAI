import os
os.system("cls")

ValorCelular = float(input("Digite o valor do celular:"))

if ValorCelular > 3000:
    print(f"O valor de R${ValorCelular} pelo celular está caro!")
else:
    print(f"O valor de R${ValorCelular} pelo celular está barato!")