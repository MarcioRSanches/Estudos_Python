from pacotes115.lib.interface import *


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!!')
    else:
        cabecalho('\033[31mErro! Digite uma opção valida!\033[m')


