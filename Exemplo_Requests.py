import requests

def retorna_dados_cep(cep):
    response = requests.get(f'http://viacep.com.br/ws/{cep}/json/')
    print(response.status_code)
    print(response.json())
    dados_cep = response.json()
    print()
    print(dados_cep['cep'])
    for i, v in dados_cep.items():
        print(f'{i} = {v}')
    print()

    return dados_cep

if __name__ == "__main__":
    #retorna_dados_cep = retorna_dados_cep()
    print(retorna_dados_cep('09520630'))
    