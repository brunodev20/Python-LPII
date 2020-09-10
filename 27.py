"""
27 - Duas amigas estabeleceram o código abaixo para que suas mensagens não
fossem lidas pelas demais pessoas.
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
&#39; &#39; a b c d e f g h i j k l m n o p q r s t u v w x y z
Observe que cada letra equivale a um número entre 1 e 26 e o espaço ao 0. Faça um
método para "traduzir", que recebe uma lista com uma mensagem (secreta) e "traduz"
a sequência armazenada em uma lista.
"""

letras = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numeros = []
traduzidos = []
digitar = True


while digitar == True:
    try:
        msg = int(input("Para enviar, utilize o comando '-1'.\nDigite um número: "))
        numeros.append(msg)

        if msg == -1:
            digitar = False
        else:
            digitar = True
    except(ValueError):
        print("Por favor, digite números.")


for n in range(len(numeros)):
    x = numeros[n]
    y = letras[x]
    traduzidos.append(y)

print("A mensagem, em forma de lista, é a seguinte:", traduzidos)
