num1 = int (input ('Diga um número: \n'))
num2 = int (input ('Diga outro número: \n'))
num3 = int (input ('Diga outro número: \n'))
if num1 == num2 and num1 == num3:
    print ('Os números são iguais.')
elif num1 > num2 and num1 > num3:
    print (num1, 'é o maior número.')
elif num2 > num1 and num2 > num3:
    print (num2, 'é o maior número.')
else:
    print (num3, ' é o maior número.')