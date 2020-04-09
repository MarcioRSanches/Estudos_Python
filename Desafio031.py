km = int(input('Qual a km da viagem? '))

'''
if km >= 200:
    print('A viagem ficou em R${:.2f}'.format(km*0.45))
else:
    print('A viagem ficou em R${:.2f}'.format(km*0.50))'''


if km >= 200:
    preço = km * 0.45
else:
    preço = km * 0.50
print('A viagem ficou em R${:.2f}'.format(preço))