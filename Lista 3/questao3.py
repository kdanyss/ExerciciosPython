name = str (input ('Diga teu nome: \n'))
while len(name) <= 3:
   name = str (input ('Inválido. Diga teu nome: \n'))

idade = int (input ('Diga tua idade: \n'))
while idade < 0 or idade > 150:
    idade = int (input ('Inválido. Diga tua idade: \n'))

salario = float (input ('Diga teu salário: \n'))
while salario < 0:
    salario = float (input ('Inválido. Diga teu salário: \n'))

sexo = input ('Sexo: f ou m \n')
while sexo != 'f' and sexo != 'm':
    sexo = input ('Inválido. Sexo: f ou m \n')

civil = input ('Estado civil s/c/n/d \n')
while civil != 's' and civil != 'c' and civil != 'n' and civil != 'd':
    civil = input ('Inválido. Estado civil s/c/n/d \n')