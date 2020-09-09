"""
24 - Receba duas listas e exiba a união destas listas e a intercalação destas listas, isto
é, 1º da 1ª lista, 1º da 2ª lista, 2º da 1ª lista, 2º da 2ª lista.
"""


lista1=[]
lista2=[]
intercalada=[]

for n in range(2):
    lista1.append(int(input("Digite os elementos da lista 1: ")))

for n in range(2):
    lista2.append(int(input("Digite os elementos da lista 2: ")))

for a,b in zip(lista1,lista2):
    intercalada.append(a)
    intercalada.append(b)

print ("União das listas:",lista1+lista2)
print ("Listas intercaladas: ", intercalada)
