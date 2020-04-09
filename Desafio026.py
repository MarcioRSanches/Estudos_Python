frase = str(input('Digite uma frase: ')).strip().upper()

print('Apareceu {} vezes a letra A'.format(frase.count('A')))
print('Apareceu a primeira vez na posição {}'.format(frase.find('A')+1))
print('Apareceu a última vez na posição {}'.format(frase.rfind('A')+1))