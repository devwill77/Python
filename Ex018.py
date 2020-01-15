'''
- DESAFIO 018
- Faça um programa que leia um ângulo qualquer e mostre na tela o valor
do seno, cosseno e tangente desse ângulo.

'''
from math import sin, cos, tan, radians
ang = float(input('Ângulo: '))
print('Seno: {:.2f}'.format(sin(radians(ang))))
print('Cosseno: {:.2f}'.format(cos(radians(ang))))
print('Tangente: {:.2f}'.format(tan(radians(ang))))


