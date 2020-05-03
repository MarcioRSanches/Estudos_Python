cont  = 0
total = 0
n     = 0
n = int(input('Digite um número: [999 p/ sair] '))
while n != 999: 
    cont  += 1
    total += n
    n = int(input('Digite um número: [999 p/ sair] '))
print('Foram {} números contados, no total de {}'.format(cont,total))    

