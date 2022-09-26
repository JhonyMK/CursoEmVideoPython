#Ler o comprimento do cateto oposto e adjacente
#Depois mostrar o comprimento da hipotenusa
#Teorema de pitagoras
''' from math import sqrt, pow
catA = float(input('Informe um lado do triangulo: '))
catB = float(input('Informe outro lado do triangulo: '))
cat = pow(catA, 2) + pow(catB, 2)
hip = sqrt(cat)
print('A soma dos catetos exponeciados é {} e hipotenusa é {}'.format(cat, hip)) '''

from math import hypot
catA = float(input('Informe um lado do triangulo: '))
catB = float(input('Informe outro lado do triangulo: '))
hip = hypot(catA, catB)
print('Sua hipotenusa vale: {}'.format(hip))