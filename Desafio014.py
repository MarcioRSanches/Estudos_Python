#CONVERSÃO DE TEMPERATURA
c = float(input('Informe a temperatura em °C:'))

f = ((9*c)/5)+32 # funciona sem os parenteses devido seguir na operação a ordem de precedentcia

print('A temperatura de {}°C corresponde a {}F'.format(c, f))
