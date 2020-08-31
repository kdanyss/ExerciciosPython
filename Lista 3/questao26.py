eleitor = int(input('Diga o número total de eleitores: \n'))
a = 0
b = 0
c = 0
ativo = 0

while ativo < eleitor:
    voto = int (input('1 = Canditado A, 2 = Candidato B ou 3 = Canditado C. \n'))
        if voto == 1:
            a = a + 1
        elif voto == 2:
            b = b + 1
        elif voto == 3:
            c = c + 1
    ativo = ativo + 1

print('Candidato A = ", a, "votos.')
print('Candidato B = ", b, "votos.')
print('Candidato C = ", c, "votos.')