peso_maior = 0
peso_menor = 0
for c in range(1,6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(c)))
    if c == 1:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso
   
print('O maior peso é {}kg e o menor é {}kg'.format(peso_maior,peso_menor))
        
    
       