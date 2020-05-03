from random import randint
from time import sleep
print('=' * 60)
print('Vou pensar em um número de 0 a 10, tente adivinhar...')
print('=' * 60)
num      = randint(0, 10)
palpites = 0

digitado = int(input('Em que número eu pensei? '))

print('\033[33mPROCESSANDO...\033[m')

sleep(2)
while num != digitado:
    if num > digitado:
        print('É maior...')
        digitado = int(input('Tente novamente!! Qual o número eu pensei? '))
    elif num < digitado:
        print('É menor...')
        digitado = int(input('Tente novamente!! Qual o número eu pensei? '))
    palpites += 1

print('Parabéns, acertou o número escolhido foi: {}, após {} palpites'.format(num, palpites))