classificacao = ('Flamento','Santos','Palmeiras','Gremio',
                'Athletico Paranaense','São Paulo','Internacional','Corinthans',
                'Fortaleza','Goiás','Bahia','Vasco da Gama',
                'Atletico','Fluminense','Botafogo','Ceará',
                'Cruzeiro','CSA','Chapecoense','Avaí')
print('=-'*20)
print(f'Lista do Brasileirão de 2019 {classificacao}')
print('=-'*20)
print(f'Os 5 primmeiros colocados foram {classificacao[0:5]}')
print('=-'*20)
print(f'Os 4 últimos colocados foram {classificacao[-4:]}')
print('=-'*20)
print(f'Lista dos times em ordem alfabética {sorted(classificacao)}')
print('=-'*20)
print(f'O Chapecoense ficou em {classificacao.index("Chapecoense")+1}º lugar')
