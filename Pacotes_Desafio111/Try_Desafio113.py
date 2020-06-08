def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
        except(KeyboardInterrupt):
            print('\033[0;31mERRO! Entrada de dados interrompida pela usuário!\033[m')
        else:
            return n
 
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido!\033[m')
        except(KeyboardInterrupt):
            print('\033[0;31mERRO! Entrada de dados interrompida pela usuário!\033[m')
        else:
            return n
 


n = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {n}')
print(f'Você acabou de digitar o número real {r}')