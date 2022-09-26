#Programa que leia o comprimento de tres retas e diga se podem ou nao formar um triangulo
#| b - c | < a < b + c
#| a - c | < b < a + c
#| a - b | < c < a + b
l1 = int(input('Digite o valor do primeiro lado: '))
l2 = int(input('Digite o valor do segundo lado: '))
l3 = int(input('Digite o valor do terceiro lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('É POSSIVEL criar um triangulo com esses segmentos!')
else:
    print('NÃO É POSSIVEL montar um triangulo com esses segmentos!')

