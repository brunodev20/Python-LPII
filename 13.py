"""
13 - Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere
que as idades dos homens serão sempre diferentes entre si, bem como as das
mulheres). Calcule e escreva a soma das idades do homem mais velho com a mulher
mais nova, e o produto das idades do homem mais novo com a mulher mais velha.
"""

idade_homens=[]
idade_mulheres=[]

for idades in range(2):
    idade_homens.append(int(input("Digite a idade do homem: ")))

for idades in range(2):
    idade_mulheres.append(int(input("Digite a idade da mulher: ")))

if idade_homens[0] == idade_homens[1] or idade_mulheres[0] == idade_mulheres [1]:
    print("As idades em um dos grupos são iguais. Reinicie o programa e tente novamente.")

else:
    print("Idade do homem mais velho + Idade da mulher mais nova =", max(idade_homens)+min(idade_mulheres))
    print("Idade do homem mais novo + Idade da mulher mais velha =", min(idade_homens)+max(idade_mulheres))
