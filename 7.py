"""
7 - Escreva um algoritmo que leia 10 números informados pelo usuário e, depois,
informe o menor, número, o maior número, a soma dos números informados e a média
aritmética dos números informados.
"""

lista=[]

for num in range(10):
    lista.append(int(input("Digite um número: ")))

print ("Os números digitados foram, respectivamente: ", lista)
print ("O menor número foi: ", min(lista))
print ("O maior número foi: ", max(lista))
print ("A soma dos números foi de: ", sum(lista))
print ("A média aritmética dos números foi de: ", sum(lista)/len(lista))

