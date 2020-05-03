razao  = int(input('Digite a razão: '))
termo  = int(input('Digite o termo: '))
cont = 1

while cont <= 10:
    print(' {} '.format(termo), end='-> ')
    termo += razao
    cont += 1
print('ACABOU')
