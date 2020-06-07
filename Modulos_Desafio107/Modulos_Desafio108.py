import moeda

valor = float(input('Digite o preço da mercadoria: R$ ' ))
taxa = float(input('Informe a taxa: '))

print(f'A metade do preço informado de R$ {valor} é de R$ {moeda.metade(valor)}')
print(f'O dobro do preço informado de R$ {valor} é de R$ {moeda.dobro(valor)}')
print(f'Um aumento do preço informado de R$ {valor} em {taxa}% é de R$ {moeda.aumentar(valor,taxa)}')
print(f'Um desconto do preço informado de R$ {valor} em {taxa}% é de R$ {moeda.diminuir(valor,taxa)}')
