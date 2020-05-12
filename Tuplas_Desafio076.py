produtos = ('Lápis',1.75,'Borracha',2.00,'Caderno',15.75,'Estojo',25,'Mochila',150)
print('.-'*15)
print(f'{"Listagem de Preços":^30}')
print('.-'*15)
for c in range(0,len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}', end='')
    if c % 2 == 1:
        print(f'R$ {produtos[c]:>7.2f}')