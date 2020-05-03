continua = 'S'
media = numero = total = maior = menor = cont = 0
while continua == 'S':
    numero = int(input('Digite um número: '))
    cont += 1
    total += numero
    media = (total/cont)
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero      
    continua = str(input('Deseja continuar? <S/N>: ')).strip().upper()
print('Digitou {} números, sendo o maior valor {} e o menor {}, com média de {}'.format(cont,maior,menor,media))   