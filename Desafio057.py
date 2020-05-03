sexo = str(input('Digite seu sexo: [M/F] ')).upper()[0].strip() # fatiamento pegando só a primeira letra upper()[0]

while sexo !='M' and sexo !='F': # sexo not in 'MnFn'
    print('Sexo inválido!!')
    sexo = str(input('Digite novamente seu sexo: [M/F] ')).upper()[0].strip()

if sexo == 'M':
    print('O sexo informado foi Masculino' )
if sexo == 'F':
     print('O sexo informado foi Feminino' )
