#Programa que pergunte o salario e o mostre seu aumento
#Salarios superiores a 1250 aumento de 10%
#Para inferiores ou iguais a 1250 aumento de 15%
s = float(input('Digite o seu sálario: '))
n1 = s * 0.10
n2 = s * 0.15
if s > 1250:
    print('O aumento de seu salario vai ser de {} com 10%, totalizando R${}'.format(n1, s + n1))
else:
    print('O aumento de seu salario vai ser de {} com 15%, totalizando R${}'.format(n2, s + n2))