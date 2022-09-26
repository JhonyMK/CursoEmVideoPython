#Programa que calcule o IMC
#Ler peso e altura
#Abaixo de 18.5 - abaixo do peso
#Entre 18.5 e 25 - peso ideal
#25 ate 30 - sobre peso
#30 ate 40 - obesidade
#Acima de 40 - obesidade morbida

from math import pow

peso = float(input('Digite seu peso(Kg): '))
altura = float(input('Digite sua altura(m): '))
imc = peso / pow(altura, 2)

print('Seu IMC é de {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso!')
elif 25 > imc >= 18.5:
    print('Peso ideal')
elif 30 > imc >= 25:
    print('Sobre peso')
elif 40 > imc >= 30:
    print('Obesidade')
else:
    print('Obesidade morbida')


