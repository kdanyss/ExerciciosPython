preco = 1.99
print('Lista de preços\n')
for x in range(1,51):
    print("%02.d - R$ %.2f"%(x, x*preco))