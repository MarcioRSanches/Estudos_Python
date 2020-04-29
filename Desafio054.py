from datetime import date

ano_atual  = date.today().year
idade      = 0
cont_maior = 0
cont_menor = 0

for c in range(1,8):
    ano_nasc = int(input('Digite o {}º ano de nascimento: '.format(c)))
    idade = ano_atual - ano_nasc
    if idade >= 18:
        cont_maior += 1
    else:
        cont_menor += 1
print('Tivemos {} pessoas maior de idade e {} menor de idade'.format(cont_maior,cont_menor))
