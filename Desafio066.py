cont = soma = 0
while True:
    num = int(input('Digite um valor: <999 p/sair> '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'soma dos {cont} valores foi {soma}')
