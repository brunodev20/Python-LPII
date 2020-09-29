"""
2 - Crie um classe Funcionário com os atributos nome, idade e salário. Deve ter
um método aumenta_salario. Crie duas subclasses da classe funcionário,
programador e analista, implementando o método nas duas subclasses. Para
o programador some ao atributo salário mais 20 e ao analista some ao salário
mais 30, mostrando na tela o valor. Depois disso, crie uma classe de testes
instanciando os objetos programador e analista e chame o método
aumenta_salario de cada um.(2,0)
"""

class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.aumento = 0

    def aumento_salario(self):
        self.salario = self.salario+self.aumento


class Programador(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)
        self.aumento = 20


class Analista(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)
        self.aumento = 30

class Test(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)
        self.aumento = 666


dev = Programador("Bruno", 25, 2500)
print("Nome do funcionário: ", dev.nome)
print("Salário: ", dev.salario)
dev.aumento_salario()
print("Salário aumentado: ", dev.salario)

ads = Analista("Cláudio", 48, 4500)
print("Nome do funcionário: ", ads.nome)
print("Salário: ", ads.salario)
ads.aumento_salario()
print("Salário aumentado: ", ads.salario)

pessoa_test = Test("Mario", 72, 210)
print("Nome: ", pessoa_test.nome)
print("Idade: ", pessoa_test.idade)
print("Ganha: ",pessoa_test.salario)

