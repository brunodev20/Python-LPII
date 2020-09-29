"""
4 - Expliquei o que é decorator e padrões de projeto. Crie um decorator que mostre
o tempo de execução de uma função que soma 4 números aleatórios. (2,0)
"""

import datetime
from random import randint

def sistema(frase):
    def açao():
        print("Iniciando programa às",datetime.datetime.now())
        print("Programa iniciado.")
        frase()
        print("Terminando programa.")
        print("Programa terminado às",datetime.datetime.now())
    return açao

@sistema
def digita_numero():
    numeros_somados=[]
    for n in range(4):
        numeros_somados.append(randint(0,1000))
    print("Os números foram: ",numeros_somados)
    print("A soma dos 4 números foi igual a: ", sum(numeros_somados))

digita_numero()
