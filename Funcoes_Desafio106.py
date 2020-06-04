def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de aluno.
    :param n: uma ou mais notas (aceita mais de uma)
    :params sit: valor opcional, indicando se mostra ou não situação Aprovado, Reprovado ou Recuperação
    :return: retorna um dicionario com o total, a maior, a menor, a media e a situação das notas
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'APROVADO'
        elif r['media'] >= 5:
            r['situacao'] = 'RECUPERAÇÃO'
        else:
            r['situacao'] = 'REPROVADO'
    return r


resp = notas(2.5, 3.8, 2.2, sit=True)
print(resp)
help(notas)