from time import sleep

print('Atenção, vai iniciar a contagem regressiva para a queima de fogos!')

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Fogo! BUMMM')

