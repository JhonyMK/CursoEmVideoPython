primeiro = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
ultimo = primeiro + (10 - 1) * razao
for c in range(primeiro, ultimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('Acabou!')