#Refazer o ex009 usando for
num = int(input('Digite um numero: '))
for c in range(0, 11):
    print('{} x {} = {}'.format(num, c, num * c))