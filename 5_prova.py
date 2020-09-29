"""
5 - Duas amigas estabeleceram o código abaixo para que suas mensagens não
fossem lidas pelas demais pessoas.
0 12 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
' ' a b c d e f g h i j k l m n o p q r s t u v w x y z
Observe que cada letra equivale a um número entre 1 e 26 e o espaço ao 0.
Faça um método para "traduzir", que recebe uma lista com uma mensagem
(secreta) e "traduz" a sequência armazenada em uma lista.
"""

def decriptar(codigo, tamanho):
    for i in range(tamanho):
        analisar = codigo[i]
        percorre_lista = encriptaçao[analisar]
        traduz.append(percorre_lista)
    print("".join(traduz))

encriptaçao = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
          'v', 'w', 'x', 'y', 'z']
codigo = []
traduz = []
funciona = True

while funciona == True:
    try:
        mensagem = int(input("Digite a mensagem: "))
        codigo.append(mensagem)
        validaçao = str(input("Efetuar tradução? 's' - sim: "))
        if validaçao == "s":
            funciona = False

    except(ValueError):
        print("Valor inválido! Digite apenas números.")

tamanho = len(codigo)

decriptar(codigo, tamanho)
