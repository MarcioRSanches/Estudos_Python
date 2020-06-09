import moeda

valor = float(input('Digite o preço da mercadoria: R$ ' ))
taxa = float(input('Informe a taxa: '))

print(f'A metade do preço informado de {moeda.real(valor)} é de {moeda.real(moeda.metade(valor))}')
print(f'O dobro do preço informado de {moeda.real(valor)} é de {moeda.real(moeda.dobro(valor))}')
print(f'Um aumento do preço informado de {moeda.real(valor)} em {taxa:.0f}% é de {moeda.real(moeda.aumentar(valor,taxa))}')
print(f'Um desconto do preço informado de {moeda.real(valor)} em {taxa:.0f}% é de {moeda.real(moeda.diminuir(valor,taxa))}')
