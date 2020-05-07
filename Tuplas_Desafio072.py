extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    numero = int(input('Digite um número [de: 0 a 20]: '))
    
    if 0 <= numero <= 20:
        print(f'O número digitado foi {extenso[numero]}') 
        resp = ' '
        while resp not in 'NS':
            resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if resp == 'N':
            break    
    else:
        print('O número digitado está fora do intervalo! ', end='' )

    


