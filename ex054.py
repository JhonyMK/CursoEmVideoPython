#Programa que leia o ano de nascimento de 7 pessoas
#Mostrar quantas são maiores de idade e quantas não são
from datetime import date
maiores = 0
menores = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    idade = date.today().year - ano
    if idade < 18:
        menores += 1
    else:
        maiores += 1
print('Ao todo tivemos {} MAIORES de idade e {} MENORES de idade!'.format(maiores, menores))