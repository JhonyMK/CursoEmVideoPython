# Estilização com cores no Python
# \033[m
# Entre o colchete e o 'm', é possível alterar o:
# Style alguns exemplos - [0, 1, 4, 7] == [none, bold, underline, negative]
# Text são cores do texto - [30, 31, 32, 33, 34, 35, 36, 37]
# Background são as cores do fundo do texto - [40, 41, 42, 43, 44, 45, 46, 47]

print('\033[7;40mOla mundo!\033[m')

nome = 'Jhony'
print('Ola! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[34m', nome, '\033[m'))

cores = {'limpa':'\033[m',
         'azul:':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Ola! Muito prazer em te conhcer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))

