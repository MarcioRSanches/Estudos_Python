print('='*20, ' L O J A S - S A N C H E S ' , '='*20)

valor = float(input('Digite o valor do produto: R$ '))

print('{:=^80}'.format(' CONDIÇÃO DE PAGAMENTO '))
print('[ 1 ] - à vista (cheque ou dinheiro) - 10% de desconto ')
print('[ 2 ] - à vista no cartão - 5% de desconto ')
print('[ 3 ] - em até 2x no cartão - preço nomral ')
print('[ 4 ] - 3x ou mais no cartão - 20% de juros')
condicao = int(input('Digite a Condição de Pagamento: '))

if condicao == 1:
    pago = valor-(valor*0.20)
elif condicao == 2:
    pago = valor-(valor*.05)
elif condicao == 3:
    pago = valor
    totparc = pago / 2 
    print('O valor de R$ {:.2f}, em 2x de R$ {:.2f}, SEM JUROS!'.format(valor,totparc))
elif condicao == 4:
   pago = valor+(valor*0.20)
   parc = int(input('Digite a quantidade de parcelas: '))
   totparc = pago / parc
   print('O valor de R$ {:.2f}, em {}x de R$ {:.2f}, COM JUROS!'.format(valor,parc,totparc))
else: 
    pago = 0
    print('Opção inválida!')
print('O valo inicial foi de $ {:.2f}, e o valor a ser pago ficou em R$ {:.2f}'.format(valor,pago))

    

