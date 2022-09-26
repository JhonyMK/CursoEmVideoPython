# calcular area de uma parede com base na largura e altura, para pinta-la sabendo que 1L de tinta pinta 2m quadrados
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2
print('Sua area é de {}m e serão necessários {}L de tinta'.format(area, tinta))