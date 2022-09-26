#Programa que leia um numero inteiro e diga se ele é primo ou não
print('Leitor de número primo')
n = int(input('Digite um numero inteiro: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi dividido {} vezes!'.format(n, total))
if total == 2:
    print('Por isso ele É PRIMO!')
else:
    print('Por isso ele NÃO É PRIMO!')