from pacotes112.utilidades import moeda
from pacotes112.utilidades import dados


valor = dados.leiaDinheiro('Digite o preço da mercadoria: R$ ' )
taxaa = float(input('Taxa de aumento: '))
taxar = float(input('Taxa de redução: '))

moeda.resumo(valor,taxaa,taxar)
#moeda.resumo(valor,taxa)