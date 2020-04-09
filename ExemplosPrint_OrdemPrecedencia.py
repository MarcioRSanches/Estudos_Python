# Ordem de Precedência
# 1) () parenteses
# 2) ** 
# 3) * / // %
# 4) + -


nome  = input('Qual o seu nome: ')
idade = input('Qual sua idade: ')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome)) #limita em 20 posições a variavel nome
print('Prazer em te conhecer {:<20}!'.format(nome)) #Alinha esquerda
print('Prazer em te conhecer {:>20}!'.format(nome)) #Alinha direita
print('Prazer em te conhecer {:^20}!'.format(nome)) #Centraliza
print('Prazer em te conhecer {:*^20}!'.format(nome)) #Centraliza e preenche os espaços com o caracter informado

print('Seu nome é: {} Sua idade é: {}!'.format(nome,idade))
print('Seu nome é: {} \n Sua idade é: {}!'.format(nome,idade)) # O \n quebra a linha do mesmo print

print('Seu nome é: {}!'.format(nome), end=' ') # O end= une o conteúdo este print e o próximo
print('Sua idade é: {}!'.format(idade))
