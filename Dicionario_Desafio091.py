from random import randint
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6),
        'jogador5': randint(1, 6)}

ordem = []

print('Resultado do jogo')
for k, v in jogo.items():
    print(f'{k} jogou o valor {v} no dado!')

ordem = sorted(jogo.items(), key=itemgetter(1), reverse=True)  
#sorted ordena o dict e o itemgetter permite ordernar pela chave = 0 ou pelo valor = 1 o reverse inverte a ordem para decrescente

print(ordem)
for i, v in enumerate(ordem):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')