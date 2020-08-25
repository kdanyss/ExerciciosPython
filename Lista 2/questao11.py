salario = float (input('Qual o seu salário?'))
if salario > 0 and salario <= 280:
    aumento = salario * 0.20
    final = salario + aumento
    print ('Seu salário era de R$', salario, 'Teve aumento de 20%, R$', aumento, '. Seu salário agora é R$', final)
elif salario > 280 and salario <= 700:
    aumento = salario * 0.15
    final = salario + aumento
    print ('Seu salário era de R$', salario, 'Teve aumento de 15%, R$', aumento, '. Seu salário agora é R$', final)
elif salario > 700 and salario <= 1500:
    aumento = salario * 0.10
    final = salario + aumento
    print ('Seu salário era de R$', salario, 'Teve aumento de 10%, R$', aumento, '. Seu salário agora é R$', final)
elif salario > 1500:
    aumento = salario * 0.05
    final = salario + aumento
    print ('Seu salário era de R$', salario, 'Teve aumento de 5%, R$', aumento, '. Seu salário agora é R$', final)
else:
    print ('Valor de salário inválido.')