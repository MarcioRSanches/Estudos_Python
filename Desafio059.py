from time import sleep

soma        = 0
multiplicar = 0
opcao       = 0 

vlr1 = int(input('Digite o primeiro número: '))
vlr2 = int(input('Digite o segundo número: '))

while opcao != 5:
    print('=-='*20)
    print('''    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos números
    [5] - Sair do programa''')
    print('=-='*20)
    opcao = int(input('>>>> Digite uma opção: '))

    if opcao == 1:
        soma = vlr1 + vlr2
        print('A soma de {} + {} é = {}'.format(vlr1,vlr2,soma))
    elif opcao == 2:
        multiplicar = vlr1 * vlr2
        print('A multiplicação de {} x {} é = {}'.format(vlr1,vlr2,multiplicar))
    elif opcao == 3:
        if vlr1 > vlr2:
            print('Entre {} e {} o maior é {}'.format(vlr1,vlr2,vlr1))
        else:
            print('Entre {} e {} o maior é {}'.format(vlr1,vlr2,vlr2))
    elif opcao == 4:
        vlr1 = int(input('Digite outro valor para o primeiro número: '))
        vlr2 = int(input('Digite outro valor para o segundo número: '))
    elif opcao == 5:
        print('Finalizando o programa!')
        sleep(2)
    else:
        print("Opção inválida, tente novamente!")


    


        
