# CRIE UM ALGORITIMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA

num    = int(input('Digite um número: '))
dobro  = num * 2
triplo = num * 3
raiz   = num ** (1/2) # ou pow(n, (1/2))

print('O dobro de ', num, ' é ' , dobro)
print('O triplo de ', num, ' é ' , triplo)
print('A raiz quadrada de ', num, ' é ' , raiz)
