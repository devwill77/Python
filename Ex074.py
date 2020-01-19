'''
 - DESAFIO 074
 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso mostre a listagem
   dos números gerados e também indique o menor e o maior valor que estão na tupla.
'''
from random import randint
números = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram -> ', end='')
for n in números:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(números)}.')
print(f'O menor valor sorteado foi {min(números)}.')











