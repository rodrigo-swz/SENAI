import os
os.system("cls")

Numero = int(input("Digite um número:"))
RestoDivisao = Numero % 2

if RestoDivisao == 0:
    print(f"O número digitado({Numero}) é PAR!")
else:
    print(f'O número digitado({Numero}) é ÍMPAR!')