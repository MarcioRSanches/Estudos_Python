import moeda

valor = float(input('Digite o preço da mercadoria: R$ ' ))
taxa = float(input('Informe a taxa: '))

print(f'A metade do preço informado de {moeda.real(valor)} é de {moeda.metade(valor, True)}')
print(f'O dobro do preço informado de {moeda.real(valor)} é de {moeda.dobro(valor, True)}')
print(f'Um aumento do preço informado de {moeda.real(valor)} em {taxa:.0f}% é de {moeda.aumentar(valor,taxa, True)}')
print(f'Um desconto do preço informado de {moeda.real(valor)} em {taxa:.0f}% é de {moeda.diminuir(valor,taxa, True)}')
