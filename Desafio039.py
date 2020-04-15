#Faça um programa que leia o ano de nascimento e informe de acordo com sua idade, se ele ainda vai se alistar ao seriço militar, se é a hora e se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano = int(input('Informe o ano de seu nascimento: '))
atual  = date.today().year
idade  = atual - ano
tempo  = ano + 18
alista = idade - 18
if idade > 18:
    print('Você tem {} anos, deveria ter se alistado {} anos atrás, em {}'.format(idade, alista, tempo ))

if idade < 18:
    print('Você tem {} anos, deverá se alistadar daqui há {} anos, em {}'.format(idade, abs(alista), tempo ))

if idade == 18:
    print('Você tem {} anos, você tem que se alestar neste ano de {}'.format(idade, tempo ))
 

    
