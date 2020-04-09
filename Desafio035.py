#pegar o comprimento de tres retas e ver se é possivel montar um triangulo
reta1 = float(input('Qual a medida da primeira reta? '))
reta2 = float(input('Qual a medida da segunda reta? '))
reta3 = float(input('Qual a medida da terceira reta? '))


if reta3 < reta2+reta1 and reta2 < reta3+reta1 and reta1 < reta2+reta3:
    print('Estas medidas PODEM formar um triangulo!')
else:
    print('Estas medidas NÃO PODEM formar um triangulo')