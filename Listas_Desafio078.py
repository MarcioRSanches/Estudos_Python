lista = []
menor = maior = 0
for pos in range(0,5):
    lista.append(int(input(f'Digite um valor para a Posição {pos}: ')))
    if pos == 0:
        maior = menor = lista[pos]
    else:
        if lista[pos] > maior:
            maior = lista[pos]
        if lista[pos] < menor:
            menor = lista[pos]
print(f'Você digitou os valores {lista}')
print(f'O maior valor da lista é {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i} -> ',end='')
print()
print(f'O menor valor da lista é {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i} -> ',end='')
print()
