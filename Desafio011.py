# FAÇA UM PROGRAMA QUE LEIA A LARGURA E ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA AREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTA-LA,
# SABENDO QUE CADA LITRO DE TINTA , PINTA UMA ARREA DE 2 METROS2

largura = float(input('Digite a largura: '))
altura  = float(input('Digite a altura '))

area  = altura * largura
tinta = 2
litros = area/tinta

print('A area calculada é: ', area)
print('Você vai precisar de ', litros,'litros de tinta')
