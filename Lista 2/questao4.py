nota1 = float (input('Digite sua primeira nota: \n'))
nota2 = float (input ('Digite sua segunda nota: \n'))
soma = nota1 + nota2
media = soma / 2
if media == 10:
    print (media, '. Aprovado com Distinção.')
elif media >= 7:
    print (media, '. Aprovado.')
else: 
    print (media, '. Reprovado.')