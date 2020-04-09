km = float(input('Qual é a velocidade atual do carro? '))

if km > 80:
    valor =(km - 80)*7
    print('MULTADO! Você execedeu o Limite que é de 80Km')
    print('Você deve pagar uma multa de R$ {:.2f}!'.format(valor))
print('Tenha um bom dia! Dirija com segurança!')