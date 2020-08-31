turmas = int(input('Número de turmas: \n'))
while turmas < 1:
    turmas = int(input('Valor inválido. Número de turmas: \n'))

cont = 1
soma = 0

while cont < turmas:
    alunos = int(input('Quantos alunos tem na turma ', cont))
        while alunos < 0 or alunos > 40:
            if alunos < 0:
                alunos = int(input('Valor inválido. Quantos alunos tem na turma ', cont, '?'))
            elif alunos > 40:
                alunos = int(input('Valor inválido. Quantos alunos tem na turma ', cont, '?'))
    soma = soma + alunos
    cont = cont + 1

print('Tem', turmas, 'turmas')
print('Tem', alunos, 'alunos')
print('Média de alunos é %.2f'%(soma/turmas))