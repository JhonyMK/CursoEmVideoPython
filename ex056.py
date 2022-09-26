#Programa que leia o nome, idade e sexo de 4 pessoas e mostre:
#A media de idade do grupo
#O nome do HOMEM mais velho
#Quantas MULHERES tem menos de 20 anos
print('Digite o nome de 4 pessoas e suas idades')
somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totMulher20 = 0
for p in range(0, 4):
    print('---{} Pessoa---'.format(p + 1))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: '))
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome

    if sexo in 'Ff' and idade < 20:
        totMulher20 =+ 1

mediaidade = somaIdade / 4
print('A media de idade do grupo é de {}'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(idade, nome))
print('O total de mulheres com menos de 20 anos é de {}'.format(totMulher20))


