from datetime import date
nasc = int(input('Informe o seu ano de nascimento: '))
idade = date.today().year - nasc

if idade <= 9:
    print('Você tem {} anos, sua categoria é MIRIM'.format(idade))
elif idade <=14:
    print('Você tem {} anos, sua categoria é INFANTIL'.format(idade))
elif idade <= 19:
    print('Você tem {} anos, sua categoria é JUNIOR'.format(idade))
elif idade <= 25:
    print('Você tem {} anos, sua categoria é SENIOR'.format(idade))
else:
    print('Você tem {} anos, sua categoria é MASTER'.format(idade))
