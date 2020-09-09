"""
23 - Crie uma programa que recebe uma lista qualquer e:
a. retorne o maior elemento 
b. retorne a soma dos elementos 
c. retorne o número de ocorrências do primeiro elemento da lista 
d. retorne a média dos elementos
"""

lista = []
contador = 5

for n in range(contador):
    lista.append(int(input("Digite um número para adicioná-lo à lista: ")))


print ("a. Maior elemento: ", max(lista))
print ("b. Soma dos elementos: ", sum(lista))
print ("c. Número de ocorrências do primeiro elemento: ", lista.count(lista[0]))
print ("d. Média dos elementos: ", sum(lista)/contador)
