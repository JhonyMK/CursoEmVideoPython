a = float(input('Digite o primeiro numero: '))
b = float(input('Digite o segundo numero: '))
c = float(input('Digite o terceiro numero: '))
# verificando o menor numero
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando o maior numero
maior = a
if b > c and b > a:
    maior = b
if c > b and c > a:
    maior = c
print('O maior valor foi {}'.format(maior))
print('O menor valor foi {}'.format(menor))
