'''
 - DESAFIO 060
 - Faça um programa que leia um número qualquer e mostre o seu fatorial.
   Ex: 5! = 5x4x3x2x1 = 120
'''
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

'''
Solução utilizando o laço For
n = int(input('Informe o número que deseja saber o fatorial: '))
f = 1
print('Calculando {}! = '.format(n), end='')
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print('{}'.format(f))
'''












