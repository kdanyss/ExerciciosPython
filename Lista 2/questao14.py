nota1 = float (input ('Diga sua primeira nota: \n'))
nota2 = float (input ('Diga sua segunda nota: \n'))
soma = nota1 + nota2
media = soma / 2
print ('Suas primeira nota foi ', nota1, ', sua segunda nota foi ', nota2)
print ('Sua média foi ', media)
if media >= 9 and media <= 10:
    print ('APROVADO - A')
elif media >= 7.5 and media < 9:
    print ('APROVADO - B')
elif media >= 6 and media < 7.5:
    print ('APROVADO - C')
elif media >= 4 and media < 6:
    print ('REPROVADO - D')
elif media >= 0 and media < 4:
    print ('REPROVADO - E')

