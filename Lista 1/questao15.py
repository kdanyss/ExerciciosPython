phora = float (input ('Quanto você ganha por hora? \n'))
pmes = float (input ('Quantas hotas você traballha por mês? \n'))
bruto = phora * pmes
IR = bruto * 0.11
INSS = bruto * 0.08
sindicato = bruto * 0.05
liquido = bruto - (IR + INSS + sindicato)
print ('Seu salário bruto é R$', bruto)
print ('Pagastes R$', IR, 'ao IR, R$', INSS, 'ao INSS e R$', sindicato, 'ao Sindicato.')
print ('Seu salário líquido é R$', liquido)