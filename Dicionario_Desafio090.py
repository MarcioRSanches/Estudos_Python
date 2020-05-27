aluno = {}
aluno['nome'] = str(input('Digite o nome do Aluno: '))
aluno['media']= float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] <= 5:
    aluno['situacao'] = 'Reprovado'
elif aluno['media'] > 5 and aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else: 
    aluno['situacao'] = 'Aprovado'

for k, v in aluno.items():
    print(f' -{k} é igual a {v}')


