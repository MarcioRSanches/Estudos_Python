time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Jogador: '))
    partidas.clear()
    total = int(input(f'Quantas partidas {jogador["nome"]}: '))
    if total != 0:
        for c in range(0, total):
            partidas.append(int(input(f'- Quantos gols na partida {c+1} ?: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continua? [S/N]: ')).upper()[0].strip()
        if resp in 'SN':
            break
        print('ERRO! - Favor digitar apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for i, j in enumerate(time):
    print(f'{i:>3} ', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)  
while True:
    busca = int(input('Digite o código do jogador, para visualizar os detalhes: (999 p/sair) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f' --- Levantamento do jogador {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+i} fez {g} gols ')
        