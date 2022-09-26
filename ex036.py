#Programa para aprovar um emprestimo bancario para comprar uma casa
#Perguntar
#Valor da casa
#Salario do comprador
#E em quantos anos ele vai pagar
#Calcular a prestação mensal sabendo que ela não pode exceder 30% do salario ou entao o emprestimo vai ser negado
casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))

prestacao = casa / (anos * 12)
valorMinimo = (salario * 0.3)

print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f} por mês.'.format(prestacao))

if prestacao > valorMinimo:
    print('Emprestimo NEGADO, pois a prestação é maior que 30%.')
else:
    print('Seu empreestimo pode ser CONCEDIDO')


