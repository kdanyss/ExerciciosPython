a = float (input ('Qual a população da cidade A? \n'))
taxaA = float (input ('Qual a a taxa de crescimento da cidade A? \n'))
b = float (input ('Qual a população da cidade B? \n'))
taxaB = float (input ('Qual a a taxa de crescimento da cidade B? \n'))
i = 0
if a < b:
    while a < b:
        a = a + (a * (taxaA/100) )
        b = b + (b * (taxaB/100) )
        i = i + 1
    print ('Demorará ', i, 'anos para A ultrapassar B')
elif b < a: 
    while b < a:
        a = a + (a * (taxaA/100) )
        b = b + (b * (taxaB/100) )
        i = i + 1
    print ('Demorará ', i, 'anos para B ultrapassar A')
else:
    print ('As cidades têm a população igual.')
