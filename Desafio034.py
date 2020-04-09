#pergunte o salario e calcule o aumento. superior a 1250 10% inferiores ou igual 15%

salario = float(input("Qual é o salário? "))

if salario > 1250.00:
    aumento = (salario*0.10)+salario
else:
    aumento = (salario*0.15)+salario
print('Seu salário é R$ {:.2f} e teve um aumento de R$ {:.2f}'.format(salario,aumento))

