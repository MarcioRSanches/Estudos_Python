pares    = []
impares  = []
completa = []
while True:
    completa.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar [S/N]: ')).upper()[0].strip()   
    if resp not in 'Ss':
        break
for i, v in enumerate(completa):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista completa é: {completa}')
print(f'A lista de números pares é: {pares}')
print(f'A lista de números ímpares é:{impares}')
    
