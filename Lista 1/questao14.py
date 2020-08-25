peso = float (input ('Qual o peso do peixe: \n'))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print ('Terá que pagar R$', multa, ' de multa.')
else: 
    print ('Não terá que pagar multa.')