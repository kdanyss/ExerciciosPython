
metros = float (input('Quantos metros quadrados tem o local que deseja pintar? \n'))
p = metros / 3
latas = p / 18
preco = latas * 80

print ('Para ', metros, 'm2 serão necessários ', '%.2f' %  latas, 'latas de tinta.')
print ('O preço a ser pago será R$', '%.2f' % preco, 'reais')
