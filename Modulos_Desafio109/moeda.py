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
