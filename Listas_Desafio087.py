matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = 0
somacoltres = 0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
    print()
for l in range(0, 3):
    somacoltres += matriz[l][2]
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print(f'A soma dos valores pares é {somapares}')
print(f'A soma dos valores da terceira coluna é {somacoltres}')
print(f'O maior valor da segunda coluna é {maior}')

