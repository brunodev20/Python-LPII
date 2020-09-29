"""
1 - Darth Vader achou que seu exército de stormtrooper estava prendendo poucos
rebeldes, então lhe contratou para desenvolver um programa que leia um conjunto
indeterminado de número de refém presos por mês. Ao final da listagem informe o
menor e o maior número de capturados, a média e o valor mais próximo a média (não
utilize funções prontas do python). (2,0)
"""

soma = 0
num_refens=0
menor_capturados = 999
maior_capturados = 0
lista=[]


while num_refens!= -1:

    num_refens = int(input("Insira o número de refens (-1 para sair): "))
    soma += num_refens

    if num_refens!= -1:
        lista.append(num_refens)

        if (num_refens < menor_capturados):
            menor_capturados = num_refens
        
        if (num_refens > maior_capturados):
            maior_capturados = num_refens

        if num_refens == -1:
            print("Programa terminado.")
            break

    media=soma/len(lista)

    for n in lista:
        if (n <= media and n > menor_capturados) or (n >= media and n < maior_capturados):
            proximo_media = n

print("Menor número: ", menor_capturados)
print("Maior número: ", maior_capturados)
print("Prisioneiros capturados por vez: ", lista)
print("Média: %.2f" % media)
print("Número mais próximo da média: ", proximo_media)
