valor = []
while True:
    numero = int(input('Digite um valor: '))

    if numero not in valor:
        valor.append(numero)
        print('Valor adicionado...')
    else:
        print('Valor duplicado! Não será adicionado...')

    resp = str(input('Deseja continuar? [S/N]: ')).upper()[0].strip()
    if resp in'Nn':
        break
valor.sort()
print(f'Os valores digitados foram: {valor}')
