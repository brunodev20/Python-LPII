"""
12 - Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior
deles.
"""

valores=[]

for n in range(2):
    valores.append(int(input("Digite um valor: ")))

if valores[0] != valores[1]:
    print (max(valores), "é o maior valor.")

else:
    print ("Os valores digitados são iguais. Reinicie o programa e tente novamente.")
