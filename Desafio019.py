#UM PROFESSOR QUER UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO
# O NOME DO ESCOLHIDO

import random

aluno1 = input('Digite o primeiro aluno: ')
aluno2 = input('Digite o segundo aluno: ')
aluno3 = input('Digite o terceiro aluno: ')
aluno4 = input('Digite o quarto aluno: ')

lista = [aluno1,aluno2,aluno3,aluno4]

print('O aluno escolhido foi {}'.format(random.choice(lista)))