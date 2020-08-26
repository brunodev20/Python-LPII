"""
6 - Faça um algoritmo que leia um nº inteiro e mostre uma mensagem indicando se este número é par ou ímpar,
e se é positivo ou negativo
"""

num=int(input("Digite um número: "))

    if num>0 and num%2==0:
        print("O número", num,"é positivo e par.")

    if num<0 and num%2==0:
        print("O número", num, "é negativo e par.")

    if num<0 and num%2!=0:
        print("O número", num, "é negativo e ímpar.")

    if num>0 and num%2!=0:
        print("O número", num, "é positivo e ímpar.")
