"""
25 - Faça uma função que receba uma lista e exiba os elementos da última metade na
frente dos elementos da primeira metade
"""

def lista_trocada(list):
    lista=[]
    metade=len(lista)/2
    invertida=lista[metade:] + lista[:metade]
    print ("Lista com as metades trocadas: ", invertida)
