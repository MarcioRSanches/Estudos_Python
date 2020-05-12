palavras = ('APRENDER', 'ESTUDAR', 'PROGRAMAR', 'AUTOMATIZAR', 'ANALISTA DE TESTES', 'PYTHON', 'ROBOT FRAMEWORK')

for c in palavras:
    print(f'\nNa palavra {c.upper()} temos ',end='')
    for vogal in c:
        if vogal.lower() in 'aeiou':
            print(vogal.lower(), end='')