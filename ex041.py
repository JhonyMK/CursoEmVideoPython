# Programa que catogorize um atleta de acordo com seu ano de nascimento
# E o coloque em uma categoria
# Ate 9 anos: Mirim
# Ate 14 anos: Infantil
# Ate 19 anos: Junior
# Ate 20 anos: Senior
# Acima: Master
from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano em que voce nasceu: '))
idade = atual - nascimento

if idade <= 9:
    print('Categoria mirim')
elif idade <= 14:
    print('Categoria infantil')
elif idade <= 19:
    print('Categoria junior')
elif idade == 20:
    print('Categoria senior')
else:
    print('Categoria master')