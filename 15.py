"""
15 - Ler 10 valores (considere que não serão lidos valores iguais) e escrever o maior
deles.
"""

valores=[]

for n in range(10):
    valores.append(int(input("Digite um valor: ")))
print(max(valores), "é o maior valor da lista.")
