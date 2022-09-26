#Refazer o ex035
#Programa que leia o comprimento de tres retas e diga se podem ou nao formar um triangulo
#E diga se o triangulo é
#Equilatero - todos os lados iguais
#Isoceles - dois lados iguais
#Escaleno - todos os lados diferentes

l1 = int(input('Digite o valor do primeiro lado: '))
l2 = int(input('Digite o valor do segundo lado: '))
l3 = int(input('Digite o valor do terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('É POSSIVEL criar um triangulo com esses segmentos!')

    if l1 == l2 == l3:
        print('O tringulo é Equilatero!')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('O triangulo é Isoceles!')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('O triangulo é Escaleno!')
    
else:
    print('NÃO É POSSIVEL montar um triangulo com esses segmentos!')
