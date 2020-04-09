#FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO ADJACENTE DE UM TRIANGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA

import math
op = float(input('Digite o comprimento do cateto oposto: '))
ad = float(input('Digite o comprimento do cateto adjacente: '))

print('A hipotenusa é {:.2f}'.format(math.hypot(op,ad)))
