soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0: # multiplo por 3
        cont = cont + 1 # contaddor dos números que são multiplos por 2
        soma = soma + c
print('A soma de {} números de 1 a 500, ímpares, multiplos por 3 é de {}'.format(cont, soma))