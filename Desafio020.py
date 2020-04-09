#O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS. FAÇA UM PROGRAMA QUE LEIA O NOME
# DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA

from random import shuffle

aluno1 = input('Digite o primeiro aluno: ')
aluno2 = input('Digite o segundo aluno: ')
aluno3 = input('Digite o terceiro aluno: ')
aluno4 = input('Digite o quarto aluno: ')

lista = [aluno1,aluno2,aluno3,aluno4]
shuffle(lista)
print('A ordem dos alunos será')
print(lista)
