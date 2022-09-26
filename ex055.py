#Programa que leia o peso de cinco pessoas, logo apos mostre o maior e o menor peso
maior = 0
menor = 0
print('Digite o peso de 5 pessoas')
for p in range(0, 5):
    peso = float(input('Peso {}: '.format(p + 1)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é de {}Kg e o menor é de {}Kg'.format(maior, menor))
    
