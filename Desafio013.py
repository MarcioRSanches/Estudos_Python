# FAÇA UM ALGORITIMO QUE LEIA O SALARIO DE UM FUNCIONARIO E MOSTRE SEU NOVO SALARIO COM 15% DE AUMENTO

sal = float(input('Digite seu salário: '))

percentual = sal * 0.15 # sal*15/100
aumento    = sal + percentual

print('Seu salário era: ', sal, 'com o aumento ficou: ', aumento)
