"""
14 - Escreva um algoritmo que calcule e imprima a tabuada do 8 (1 a 10).
"""

num=int(input("Digite um número para exibir sua tabuada: "))
cont=1

while cont<=10:
    print (num, "X", cont, "=", num*cont)
    cont+=1
