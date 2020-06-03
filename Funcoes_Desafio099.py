from time import sleep

def maior(* num):  # 0 * indica que é empacotamento de valores... não sabemos quantos números serão inseridos
    cont = maior = 0
    print('-='* 30)
    print('Analisando os valores passados....')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(9,5,7,8,10,5,1)
maior(2,5,7,1,0)
maior(-5,0,1)
maior(2)
maior()