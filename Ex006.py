'''
- DESAFIO 006
- Crie um algoritmo que leia um número e mostre o seu dobro,
triplo e raiz quadrada.
'''
num = float(input('Digite um número: '))
print('O número digitado foi {:.1f}, seu dobro é {:.1f}, seu triplo é {:.1f} '
      ' e sua raíz quadrada é {:.1f}'.format(num, num * 2, num * 3, num**(1/2)))

