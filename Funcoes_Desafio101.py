def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não Vota'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto Opcional'
    else:
        return f'Com {idade} anos: Voto Obrigatório'

print('-+' * 20)
print(voto(2003))
print(voto(2012))
print(voto(1942))
print(voto(1972))
print('-+' * 20)

nasc = int(input('Digite o ano de nascimento: '))
print(voto(nasc))
