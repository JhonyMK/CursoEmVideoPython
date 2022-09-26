# Programa que calcule a soma entre todos os numeros impares, que sao multiplos
# de 3 entre 1 e 500
print('Numeros impares de 1 ate 500')
soma = 0
contador = 0
for c in range(0, 501):
    if c % 2 == 1 and c % 3 ==0:
        contador += 1 #contador = contador + 1
        soma += 1 #soma = soma + 1
print(soma)
print(contador)