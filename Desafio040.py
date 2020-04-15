nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2

if media >= 7:
    print('Sua nota1 foi {:.2f} e sua nota2 {:.2f}, com a média {:.2f} - Está APROVADO!'.format(nota1,nota2,media))
elif media >= 5 and media <= 6.9:
    print('Sua nota1 foi {:.2f} e sua nota2 {:.2f}, com a média {:.2f} - Está de RECUPERAÇÃO!'.format(nota1,nota2,media))
elif media < 5:
    print('Sua nota1 foi {:.2f} e sua nota2 {:.2f}, com a média {:.2f} - Está de REPROVADO!'.format(nota1,nota2,media))