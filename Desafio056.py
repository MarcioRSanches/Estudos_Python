soma_idade  = 0
media_idade = 0
idade_maior = 0
cont_mulher = 0
homem_velho = ''


for c in range (1,5):
    print('===== Dados da {}ª pessoa ====='.format(c))
    nome  = str(input('Digite o nome : '))
    idade = int(input('Digite a idade: '))
    sexo  = str(input('Digite o sexo [M]/[F]: ')).strip().upper()

    soma_idade += idade
    media_idade = soma_idade/c    

    if sexo == 'M' and idade > idade_maior:
        idade_maior = idade
        homem_velho = nome

    if sexo == 'F' and idade < 20:
        cont_mulher += 1

print('A média de idade do grupo é {:.0f} anos'.format(media_idade))
print('O homem mais velho tem {} anos e chama-se {}'.format(idade_maior,homem_velho))
print('Temos {} mulheres com menos de 20 anos'.format(cont_mulher))
    

    

 




