jogador = {}
partidas = []
jogador['nome'] = str(input('Jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]}: '))
if total != 0:
    for c in range(0, total):
        partidas.append(int(input(f'- Quantos gols na partida {c+1} ?: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
partidas.clear()
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v} ')
print('-='*30)
print(f' O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f' ** Na partida {i+1}, fez {v} gols')
print(f'Total de gols: {jogador["total"]}')
