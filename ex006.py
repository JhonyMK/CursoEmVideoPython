num = int(input('Escolha um número: '))
dobro = num * 2
triplo = num * 3
# raiz = num ** (1/2)
raiz = pow(num, (1/2))
print('O dobro de {} é {}, seu triplo é {} e sua raiz quadrada é {}'.format(num, dobro, triplo, raiz))