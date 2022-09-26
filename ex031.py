#Perguntar a distancia da viagem em km
#Para viagens até 200km cobrar 0.50 por km
#E 0.45 para viagens mais longas
v = int(input('Distancia da viagem: '))
x = v * 0.5
y = v * 0.45
if v <= 200:
    print('Sua viagem vai custar R${}'.format(x))
else:
    print('A distancia é maior que 200km')
    print('Sua viagem vai custar R${}'.format(y))