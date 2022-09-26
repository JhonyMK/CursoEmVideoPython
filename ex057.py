#Programa que leia o sexo de uma pessoa, mas so aceite as opções M ou F

sexo = input(str('Sexo [M/F]: ')).upper()
while sexo != 'M' or 'F':
    input('Erro digite novamente: ')
print('FIM')