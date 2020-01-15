'''
- DESAFIO 012
- Faça um algoritmo que leia o preço de um produto e mostre
seu novo preço com 5% de desconto.
'''
preço = float(input('Informe o preço do produto: R$'))
novo_preço = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f} com 5% de desconto passou a custar R${:.2f}'.format(preço, novo_preço))


