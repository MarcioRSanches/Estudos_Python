from pacotes111.utilidades import dados
from pacotes111.utilidades import moeda


valor = leiaFloat('Digite o preço da mercadoria: R$ ' )
taxaa = float(input('Taxa de aumento: '))
taxar = float(input('Taxa de redução: '))

moeda.resumo(valor,taxaa,taxar)
#moeda.resumo(valor,taxa)