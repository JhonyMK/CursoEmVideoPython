#Randomizar um número entre 0 e 5 e fazer o usuario tentar adivinhar
from random import randint
from time import sleep
n = randint(0, 5)
x = int(input('Escolha um número entre 0 e 5: '))
print('Processando!')
sleep(2)
print('O programa escolheu o numero: {}'.format(n))
if x == n:
    print('Parabens voce acertou!')
else:
    print('Voce errou tente denovo na proxima!')
