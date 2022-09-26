nome = str(input('Qual seu nome? '))
if nome == 'Jhony':
    print('Que nome bonito!')
elif nome == 'Joao' or 'Maria' or 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))