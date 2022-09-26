#Programa que leia o ano de nascimento de um jovem e informe
#Se ele ainda vai se alistar
#Se é hora de se alistar
#Ou se ja passou do tempo
#O programa deve mostrar quanto tempo falta ou que passou para o alistamento
from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
tempoMaior = idade - 18
tempoMenor = 18 - idade

#Menor de idade
if idade < 18:
    print('Voce nao possui idade para de se alistar!')
    print('Faltam {} anos para voce poder se alistar!'.format(tempoMenor))
elif idade == 18:
    print('Voce ja pode se alistar!')
elif idade > 18:
    print('Caso voce nao tenha se alistado, ja passou da hora!')
    print('Ja se passaram {} anos, tem multa em cuidado fih!'.format(tempoMaior))