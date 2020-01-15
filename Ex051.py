'''
 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
   primeiros ternos dessa progressão.
'''
print('+' * 22)
print('PROGRESSÃO ARITMÉTICA')
print('+' * 22)
p_termo = int(input('Informe o 1° termo da PA: '))
raz = int(input('Informe a razão da PA: '))
dec = p_termo + (10 - 1) * raz
for c in range(p_termo, dec + raz, raz):
    print('{} '.format(c), end='-> ')
print('FIM')






