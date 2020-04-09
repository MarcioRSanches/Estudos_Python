from random import randint
from time import sleep
print('=' * 60)
print('Vou pensar em um número de 0 a 5, tente adivinhar...')
print('=' * 60)
num = randint(0, 5)

digitado = int(input('Em que número eu pensei? '))

print('\033[33mPROCESSANDO...\033[m')

sleep(2)

if num == digitado:
    print('Parabéns, acertou o número escolhido foi: {}'.format(num))
else:
    print('Tente novamente, infelizmente erro, o número escolhido foi: {}'.format(num))
