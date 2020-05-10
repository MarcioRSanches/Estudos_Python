from random import randint
v = 0
while True:
    jogador    = int(input('Informe um valor: '))
    computador = randint(0, 10)
    total      = jogador + computador
    par_impar  = ' '
    while par_impar not in 'PI':
        par_impar = str(input("Par ou Ímpar?  <P/I> ")).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR')
    if par_impar == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif par_impar == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Voce PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER Você VENCEU {v} vezes')
