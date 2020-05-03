n     = int(input('Quantos termos [FIBONACCI], você quer mostrar? '))
ant   = 0
post  = 1
cont  = 0
print('{} -> {}'.format(ant, post),end='')
while cont <= n:
    atual = ant + post
    print( '-> {}'.format(atual),end='')
    ant   = post
    post  = atual
    cont += 1
print('-> FIM!')
