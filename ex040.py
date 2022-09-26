#Programa que le 2 notas de um aluno e mostra a media
#Media abaixo de 5 REPROVADO
#Media entre 5 e 6.9 RECUPERACAO
#Media 7 ou superior APROVADO
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2
print(media)

if media < 5:
    print('REPROVADO!')
elif 6.9 >= media >= 5:
    print('RECUPERAÇãO!')
elif media >= 7:
    print('APROVADO!')