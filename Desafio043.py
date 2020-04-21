peso   = float(input('Digite seu peso: Kg '))
altura = float(input('Digite sua altura: M '))

imc = peso/(altura*altura)

print('Seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc < 25:
    print('Você está com o PESO IDEAL!')
elif imc < 30:
    print('Você está com SOBREPRESO!')
elif imc < 40:
    print('Você esá com OBESIDADE!')
else: 
    print('Você esá com OBESIDADE MÓRBIDA!')
