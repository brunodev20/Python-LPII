"""
28 - Faça um programa que percorre uma lista e exiba na tela o valor mais próximo da
média dos valores da lista. Exemplo: lista = [2.5, 7.5, 10.0, 4.0] (média = 6.0). Valor
mais próximo da média = 7.5
"""

lista=[]
contador=5


for n in range(contador):
    lista.append(int(input("Digite um número: ")))

media= sum(lista)/contador
diffs = {value: abs(value - media) for value in lista}

print ("Média da lista: ", media)
print ("Valor mais próximo: ", diffs)
