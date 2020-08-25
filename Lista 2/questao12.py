phora = float (input ('Quanto você ganha por hora? \n'))
pmes = float (input ('Quantas horas você trabalha por mês? \n'))
bruto = phora * pmes
FGTS = bruto * 0.11
sindicato = bruto * 0.03
if bruto > 0 and bruto <= 900:
    IR = 0
elif bruto > 900 and bruto <= 1500:
    IR = bruto * 0.05
elif bruto > 1500 and bruto <= 2500:
    IR = bruto * 0.10
elif bruto > 2500:
    IR = bruto * 0.20
else:
    print ('Você não recebe salário.')
liquido = bruto - (IR + sindicato)
print ('Seu salário bruto é R$', bruto)
print ('A empresa pagou', FGTS, 'ao FGTS')
print ('Você pagpu R$', IR, 'ao IR e R$', sindicato, 'ao Sindicato.')
print ('Seu salário líquido é R$', liquido)