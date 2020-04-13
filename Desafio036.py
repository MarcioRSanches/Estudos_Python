casa      = float(input('Qual o valor da casa? R$ '))
salario   = float(input('Qual o salário? R$ '))
ano       = float(input('Em quantas vezes pagará? '))

prestacao = (casa /(ano*12))
minimo    = (salario*0,30)

print('O valor da prestação ficou em R$ {:.2f}'.format(prestacao))

if (prestacao) > (salario*0.30):
    print('O empréstimo foi NEGADO, o valor da parcela R$ {:.2f} é superior a 30% do seu salário que é R$ {:.2f}'.format(prestacao, minimo))
else:
    print('Parabéns seu empréstimo foi aprovado!')
