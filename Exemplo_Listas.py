galera = []
dados  = []
maior = menor = 0

for c in range(0, 3):
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite a idade: ')))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] > 21:
        print(f'{p[0]}, tem {p[1]} anos, é MENOR de idade')
        maior += 1
    else:
        print(f'{p[0]}, tem {p[1]} anos, é MAIOR de idade') 
        menor += 1
  
print(f'Temos {maior} maiores de idade e {menor} menores de idade')
