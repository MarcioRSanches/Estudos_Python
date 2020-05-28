def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}m x {comprimento}m é de {a}m².')


print('Controle de terrenos')
l = float(input('Largura: (m) '))
c = float(input('Comprimento: (m) '))
area(l, c)

