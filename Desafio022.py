nomecompleto = str(input('Digite o seu nome completo: ')).strip()

print('Analisando seu nome....')
print('Seu nome em maiúsculas é {} '.format(nomecompleto.upper()))
print('Seu nome em minúsculas é {} '.format(nomecompleto.lower()))
print('Seu nome apenas com a primeira letra maiúscula é {}'.format(nomecompleto.capitalize()))
print('Seu nome e sobrenome com a primeira letra maiúscula é {} '.format(nomecompleto.title()))
print('Seu nome tem ao todo, {} letras'.format(len(nomecompleto)-nomecompleto.count(' '))) # conta quantos caracteres removendo os espaços antes de depois da frase
print('Seu primeiro nome tem, {} letras'.format(nomecompleto.find(' ')))
separa = nomecompleto.split()
print(separa)
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
