'''
- DESAFIO 017
- Faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

'''
from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hip = hypot(ca,co)
print('Hipotenusa: {:.2f}'.format(hip))

