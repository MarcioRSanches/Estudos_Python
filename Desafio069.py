soma_maior18 = soma_sexoF_menor20 = soma_sexoM = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo  = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
    print('-'*20)

    if idade > 18:
        soma_maior18 += 1
    if sexo == 'M':
        soma_sexoM += 1
    if sexo == 'F' and idade < 20:
        soma_sexoF_menor20 += 1

    continua = str(input('Deseja continuar [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
    
print(f'Total de pessoas com mais de 18 anos: {soma_maior18}')
print(f'Total de homens cadastrados: {soma_sexoM}')
print(f'Total de mulheres menos de 20 anos: {soma_sexoF_menor20}')