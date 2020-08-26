print('Digite uma valor')
valor = int(input())

print('Digite o preço')
preco = int(input())

desc = int(input("Digite o valor do desconto: "))
total = preco - desc
print ('O preço com desconto é R${}'.format(total))

troco = valor - total

print('O valor do troco será R${}'.format(troco))
