num = int(input('Digite um numero: '))

print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {} '.format(num, bin(num) [2:])) 
    # o [2:] é o fatiamento para não aparecer as duas primeiras letras que são iguais para cada tipo
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {} '.format(num, oct(num) [2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {} '.format(num, hex(num) [2:]))
else:
    print('Opção inválida. Tente novamente.')


