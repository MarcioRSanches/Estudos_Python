import math #IMPORTA TODA A BIBLIOTECA
# from math import sqrt, ceil # IMPORTA APENAS DA BIBLIOTECA MATH O SQRT E CEIL

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz de {} é {}'.format(num, raiz)) 
print('A raiz de {} é {:.2f}'.format(num, raiz)) # CONFIGURANDO A FORMATAÇÃO DE 2 CASAS DE DECIMIAS PARA A RAIZ
print('A raiz de {} é {}'.format(num, math.ceil(raiz))) # CEIL ARREDONDA PRA CIMA