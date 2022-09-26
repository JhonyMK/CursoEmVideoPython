# Programa que calcule o valor a ser pago em um produto
# Considerando seu preço normal e a condição de pagamento
# A vista no dinheiro/cheque: 10% de desconto
# A vista no catão: 5% de desconto
# Em ate 2x no catão: preço normal
# 3x ou mais no catão: 20% de juros

produto = int(input('Valor do produto a ser pago: '))
print('Valor cheio do produto: {}'.format(produto))

print('1 - pagamento a vista no dinheiro ou cheque (10% de desconto) \n'
      '2 - pagamento a vista no cartao (5% de desconto) \n'
      '3 - parcela de ate 2x no cartao (preço normal) \n'
      '4 - parcela de 3x ou mais no cartao (20% de juros) \n')
valor = str(input('Escolha a forma de pagamento: '))

if valor == '1':
    print('O total com 10% de desconto: {}'.format(produto - (produto * 0.10)))
elif valor == '2':
    print('O total com 5% de desconto: {}'.format(produto - (produto * 0.05)))
elif valor == '3':
    print('Nao será alterado o valor {}, valor parcelado: {}'.format(produto, produto / 2))
elif valor == '4':
    total = produto + (produto * 0.20)
    totalparc = int(input('Quantas parcelas: '))
    parcela = total / totalparc
    print('Sua compra sera parcelada em {}x de R${:.2f} com JUROS'.format(totalparc, parcela))
    print('O preço total será de {}'.format(total))
else:
    print('Opção invalida!')
