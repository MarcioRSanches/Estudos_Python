def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato is False else real(res)

def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else real(res)

def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else real(res)

def metade(preco=0,formato=False):
    res = preco / 2
    return res if not formato else real(res)

def real(preco=0, real='R$ '):
    return f'{real}{preco:>.2f}'.replace('.',',')

def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO PREÇO DA MERCADORIA'.center(30))
    print('-' * 30)
    print(f'Preço: {real(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-' * 30)