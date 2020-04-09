num = int(input('Digite um número: '))
n = str(num)
u = num // 1 % 10 # pega o resto da divisão
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('A milhar é: {}'.format(m))
print('A centena é: {}'.format(c))
print('A dezena é: {}'.format(d))
print('A unidade é : {}'.format(u))
