from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Informe a sua opção:
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura''')
jogador = int(input('Escolha sua jogada: '))

print('Jo...')
sleep(1)
print('ken...')
sleep(1)
print('po!!!!!')
sleep(1)
print('~'*50)
print('Computador: Jogou {}'.format(itens[computador]))
print('Jogador: Jogou {}'.format(itens[jogador]))
print('~'*50)

if computador == 0:
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('O JOGADOR VENCEU')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU ')
    else:
        print('JOGADA INVAÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('O COMPUTADOR VENCEU ')
    elif jogador == 1:
        print('EMPATOU')
    elif jogador == 2:
        print('O JOGADOR VENCEU')
    else:
        print('JOGADA INVAÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('O JOGADOR VENCEU')
    elif jogador == 1:
        print('O COMPUTADOR VENCEU ')
    elif jogador == 2:
        print('EMPATOU')
    else:
        print('JOGADA INVAÁLIDA')
        