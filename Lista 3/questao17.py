n = int (input('Diga um número: \n'))
fat = 1
while n > 1:
    fat = fat * n
    n = n - 1
print ('O fatorial é ', fat)