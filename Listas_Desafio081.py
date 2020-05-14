valor = []
while True:
    valor.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N]: ')).upper()[0].strip()
    if resp in 'Nn':
        break
print('-='*20)
print(f'A quantidade de itens da lista é: {len(valor)}')
valor.sort(reverse=True)
print(f'A lista em ordem descrescente é: {valor}')
if 5 in valor:
    print('O número cinco está na lista!')
else:
    print('O número cinco NÃO está na lista!')