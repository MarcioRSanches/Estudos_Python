lista = []
for c in range (0,5):
    numero = int(input('Digite um número: '))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Adiciooando número no final da lista!')
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos,numero)
                print(f'Adicionando número na posição {pos} da lista!')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados na lista foram: {lista}')