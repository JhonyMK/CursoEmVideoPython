#Ler um angulo qualquer
#Mostrar seu seno e seu cosseno
from math import cos, sin, tan, radians
num = float(input('Digite o angulo desejado: '))
c = cos(radians(num))
s = sin(radians(num))
t = tan(radians(num))
print('Seu COSSENO é {:.2f}, seu SENO é {:.2f} e sua TANGENTE é {:.2f}'.format(c, s, t))
