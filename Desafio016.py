#CRIE UM PROGRAMA QUE LEIA UM NUMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA A SUA POSICAO INTEIRA
#EXEMPLO: DIGITE UM NÚMERO: 6.127
#O NYNERIO 6.127 TEM A PART INTEIRA 

import math

num     = float(input('Digite um número: '))


print('O número digitado foi {} e será exibido a parte inteira: {}'.format(num, math.trunc(num)))
