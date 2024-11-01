import os
os.system("cls")

NomeAluno = input("Digite o nome do aluno:")
Materia = input("Digite a matéria:")
Nota1 = float(input("Digite a primeira nota:"))
Nota2 = float(input("Digite a segunda nota:"))
Media = float((Nota1+Nota2)/2)

print(f"O(a) aluno(a) {NomeAluno} teve a média final de {Media} na matéria {Materia}!")