# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS

metro = int(input('Digite a quantidade de metros para serem convertidos: '))

centimetros = metro*100
milimetros  = metro*1000

print(metro, 'metro(s), equivale a ', centimetros, 'cm e ', milimetros, 'mm')
