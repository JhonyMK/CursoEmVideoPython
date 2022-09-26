import random
from random import shuffle
y = str(input('Primeiro aluno: '))
x = str(input('Segundo aluno: '))
z = str(input('Terceiro aluno: '))
a = str(input('Quarto aluno: '))
lista = [y, x, z, a]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)