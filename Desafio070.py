print('{:=^40}'.format(' LOJA TEM DE TUDO '))
maior = total = menor = cont = 0
nome = ''
while True:
    prod = str(input('Digite o produto: '))
    prec = float(input('Digite o valor R$ '))
    cont += 1
    total += prec
    if prec > 1000:
        maior += 1
    if  cont == 1 or prec < menor:
        menor = prec
        nome  = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continua? [S/N]: ')).upper()[0].strip()
    if resp != 'S':
        break
print('{:=^40}'.format(' RESUMO DA COMPRA '))
print(f'Total da compra ficou em R$ {total:.2f}')
print(f'Produtos acima de R$ 1000,00, foram {maior}')
print(f'O produto mais barato foi {nome} com o valor de R$ {menor:.2f}')