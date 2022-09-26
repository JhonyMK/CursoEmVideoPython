nome = input('Digite seu nome completo: ')
# separado = nome.split()
primeiro = nome.split()[0]
ultimo = nome.split()[-1]
print('''Nome completo: {} \n
Primeiro nome: {} \n
Ultimo nome: {}'''.format(nome, primeiro, ultimo))