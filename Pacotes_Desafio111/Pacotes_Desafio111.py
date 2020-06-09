from Pacotes_Desafio111.utilidades import dado
from Pacotes_Desafio111.utilidades import moeda


valor = leiaFloat('Digite o preço da mercadoria: R$ ' )
taxaa = float(input('Taxa de aumento: '))
taxar = float(input('Taxa de redução: '))

moeda.resumo(valor,taxaa,taxar)
#moeda.resumo(valor,taxa)