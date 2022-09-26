#Ler a velocidade do carro
#Se estiver acima de 80km aplicar uma multa de R$7 por cada km a mais

v = int(input('Digite a velocidade do carro: '))
multa = (v - 80) * 7
if v > 80:
    print('Voce esta sendo multado por excesso de velocidade! \n'
          'Valor da multa: R${}'.format(multa))
else:
    print('Tudo certo boa viajem!')