"""
16 - Faça um algoritmo que leia os valores de COMPRIMENTO, LARGURA e ALTURA
e apresente o valor do volume de uma caixa retangular. Utilize para o cálculo a fórmula
VOLUME = COMPRIMENTO * LARGURA * ALTURA.
"""

comprimento=float(input("Digite o valor do comprimento: "))
largura=float(input("Digite o valor da largura: "))
altura=float(input("Digite o valor da altura: "))

volume= comprimento * largura * altura

print("O volume é igual a: %.2f" % volume)
