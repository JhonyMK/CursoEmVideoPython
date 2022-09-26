dias = int(input('Por quantos dias o carro foi alugado: '))
km = float(input('Quantos km foram rodados: '))
total = (60 * dias) + (0.15 * km)
print('Foram alugados {} dias com {}km rodados, total de R${}'.format(dias, km, total))