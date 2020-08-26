"""
10 - receba três notas de um aluno e informe se ele passou ou reprovou.
"""

aluno1=[]


for notas in range(3):
    aluno1.append(float(input("Digite a nota do aluno: ")))


if (sum(aluno1)/3) >= 7:
    print("Média: %.2f" % (sum(aluno1)/3), "| O aluno foi aprovado!")

else:
    print("Média: %.2f" % (sum(aluno1)/3),"| O aluno foi reprovado.")
