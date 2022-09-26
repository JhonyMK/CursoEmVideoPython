#Programa que sorteia o nome entre 4 alunos
from random import choice
y = str(input('Primeiro aluno: '))
x = str(input('Segundo aluno: '))
z = str(input('Terceiro aluno: '))
a = str(input('Quarto aluno: '))
lista = [y, x, z, a]
aluno = choice(lista)
print('O aluno escolhido foi {}'.format(aluno))