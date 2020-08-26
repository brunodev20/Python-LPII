"""
9 - Faça um método que receba um número X e uma palavra no console e repita x
vezes a essa frase.
"""

x=int(input("Digite um número. Este número será o número de vezes que a palavra que você digitar se repetirá: "))
palavra=input("Digite uma palavra: ")

print((palavra+"\n")*x)
