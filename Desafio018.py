# FAÇA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ANGULO
import math
an = float(input('Digite o angulo: '))

print('O valor do seno é {:.2f}'.format(math.sin(math.radians(an))))
print('O valor do cosseno é {:.2f}'.format(math.cos(math.radians(an))))
print('O valor do tangente é {:.2f}'.format(math.tan(math.radians(an))))