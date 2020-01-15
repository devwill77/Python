'''
 - DESAFIO 036
 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
   Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
   A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
valor_casa = float(input('Informe o valor da casa: R$'))
salário = float(input('Informe o salário do comprador: R$'))
qt_anos = int(input('Informe a quantidade de anos em que será pago a casa: '))
parcela = valor_casa / (qt_anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor_casa, qt_anos), end='')
print(' a parcela será de R${:.2f}'.format(parcela))
if parcela <= mínimo:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')







