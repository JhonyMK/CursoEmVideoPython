# Programa que jogue jokenpo com o usuario
import random
from random import randint
from time import sleep
variaveis = ('pedra', 'papel', 'tesoura')
cpu = randint(0, 2)
variaveisCPU = variaveis[cpu]

print('Vamos jogar jokenpo! \n'
      '0 - Pedra \n'
      '1 - Papel \n'
      '2 - Tesoura \n')
jogador = int(input('Escolha uma opçõe: '))
variaveisJogador = variaveis[jogador]
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('CPU jogou {}'.format(variaveisCPU))
print('O jogador jogou {}'.format(variaveisJogador))

if cpu == 0: #CPU jogando PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('CPU VENCE!')
    else:
        print('Opção invalida!')

if cpu == 1: #CPU jogando PAPEL
    if jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    elif jogador == 0:
        print('CPU VENCE!')
    else:
        print('Opção invalida!')

if cpu == 2: #CPU jogando TESOURA
    if jogador == 2:
        print('EMPATE!')
    elif jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('CPU VENCE!')
    else:
        print('Opção invalida!')

