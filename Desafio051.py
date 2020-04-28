razao  = int(input('Digite a razão: '))
termo  = int(input('Digite o termo: '))
decimo = termo + (10 - 1) * razao

for c in range(termo,decimo,razao):
    print(' {} '.format(c), end='-> ')
print('ACABOU')

