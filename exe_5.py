class Validar:
    def validar_numero(self, n1):
        if n1 >= 0:
            if n1 % 2 == 0:
                print ("O número é positivo e par")
            else:
                print ("O número é positivo e ímpar")
        else:
            #validação de impares
            if n1 % 2 == 0:
                print ("O número é negativo e par")
            else:
                print ("O número é negativo e ímpar")

validar = Validar()
num = int(input("Digite um numero: "))

validar.validar_numero(num)
