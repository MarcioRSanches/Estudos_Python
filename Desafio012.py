#  FAÇA UM ALGORÍTIMO QUE LEIA O PREÇO DE UM PRODUTO SEU NOVO PRECO COPM 5% DE DESCONTO

valor = float(input('Digite o valor do produto: '))

percentual = (valor*0.05) # valor*5/100
desconto   = (valor-percentual)

print('O valor do produto é: ', valor, 'com desconto sairá:' , desconto)

