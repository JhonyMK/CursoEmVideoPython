#Programa que leia 2 numeros inteiros e compare-os
#Mostrando
#Qual é maior
#Qual é o menor
#E se nao houver diferenca printar que nao ha diferenca
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n1 > n2:
    print('O primeiro numero é maior! ')
elif n1 < n2:
    print('O segundo numero é maior!')
elif n1 == n2:
    print('Os dois sao iguais!')