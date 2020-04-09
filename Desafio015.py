km  = float(input('Digite a quantidade de km rodado: KM '))
dia = int(input('Digite quantos dias utilizou o carro: '))

vlrdia = dia*60
vlrkm  = km*0.15

vlrkmrodado = vlrdia+vlrkm

print('O custo total do km rodado: R${:.2f}'.format(vlrkmrodado))
