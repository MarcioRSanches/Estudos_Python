ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota1)/2
    ficha.append([nome, [nota1, nota2], media])
    resp = (str(input('Deseja continuar [S/N]:')))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 26)
for i, v in enumerate(ficha):
    print(f'{i:<4}{v[0]:<10}{v[2]:>8.1f}')
while True:
    print('-'* 35)
    detalhe = int(input('Mostrar notas de qual aluno? [999 p/ sair]: '))
    if detalhe == 999:
        print('Finalizando ... ')
        break
    if detalhe <=len(ficha) - 1:
        print(f'Notas de {ficha[detalhe][0]} são {ficha[detalhe][1]}')
print('<<< VOLTE SEMPRE >>>')