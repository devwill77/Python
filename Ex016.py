'''
- DESAFIO 016
- Crie um programa que leia um número real qualquer pelo teclado
e mostre na tela sua porção inteira.

Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6
'''
from math import trunc

num = float(input('Informe um número real qualquer: '))
res = trunc(num)
print('A parte inteira do número {} é {}'.format(num, res))






