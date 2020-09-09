"""
26 - Faça um programa que receba duas listas e retorne True se são iguais ou False
caso contrário, além do número de ocorrências do primeiro elemento da lista.
"""

lista1=[]
lista2=[]

for n in range(6):
    lista1.append(int(input("Digite um número para a lista 1: ")))

for n in range(6):
    lista2.append(int(input("Digite um número para a lista 2: ")))

if lista1==lista2:
    print(True)
else:
    print(False)

print ("Número de ocorrências do primeiro elemento na lista 1: ", lista1.count(lista1[0]))
print ("Número de ocorrências do primeiro elemento na lista 2: ", lista2.count(lista2[0]))
