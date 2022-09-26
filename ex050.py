#Programa que leia 6 numeros inteiros e moste apenas os pares
print('Digite 6 número inteiros')
soma = 0
cont = 0
for c in range(0, 6):
    c += 1
    n = int(input('{} numero: '.format(c)))
    if n % 2 == 0:
        cont += 1
        soma += n
print('Os números pares são {} e a soma de deles é {}'.format(cont, soma))




