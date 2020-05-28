def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {a}m².')


print('Controle de terrenos')
l = float(input('Largura: '))
c = float(input('Comprimento: '))
area(l, c)

