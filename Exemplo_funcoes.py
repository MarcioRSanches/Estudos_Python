def contador(i, f, p):
    # abaixo é a criação de uma docstring
    """ 
    -> Faz uma contagem e mostra na tela;
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno

    """
    c = 1
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


#execução funcão
contador(1,10,2)

#execuçao docstring da funcao
help(contador)

#parametro opcionais
def somar(a=0,b=0,c=0):
    soma = a+b+c
    print(f'A soma é {soma}')

somar(2,5)
somar(b=3,c=6)

