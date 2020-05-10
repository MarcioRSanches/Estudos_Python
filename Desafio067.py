
while True:
    tab = int(input('Digite um número para sua tabuada: '))
    print('=-'*5, 'TABUADA DO', tab, '=-' *5)
    if tab < 0:
        break
    for cont in range(0,11):
        print(f'{tab} x {cont} = {tab*cont}')
    print('=-'*18)
 
    
