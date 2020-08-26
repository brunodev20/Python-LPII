class Calculadora:

    def calcular_soma(self, n1, n2):
        soma = n1 + n2
        print('{} + {} = {}'.format(n1, n2, soma))

    def calcular_subtracao(self, n1, n2):
        subtracao = n1 - n2
        print('{} - {} = {}'.format(n1, n2, subtracao))

    def calcular_multiplicacao(self, n1, n2):
        multiplicacao = n2 * n1
        print('{} * {} = {}'.format(n1, n2, multiplicacao))

    def calcular_divisao(self, n1, n2):
        divisao = n2 / n1
        print('{} / {} = {}'.format(n1, n2, divisao))


calcular = Calculadora()

print('Digite o número 1: ')
n1 = int(input())

print('Digite o número 2: ')
n2 = int(input())

calcular.calcular_soma(n1, n2)
calcular.calcular_subtracao(n1, n2)
calcular.calcular_multiplicacao(n1, n2)
calcular.calcular_divisao(n1, n2)

print ("\nResultados com acréscimo 1:")
calcular.calcular_soma(n1, n2+1)
calcular.calcular_subtracao(n1, n2+1)
calcular.calcular_multiplicacao(n1, n2+1)
calcular.calcular_divisao(n1, n2+1)
