'''
 - DESAFIO 035
 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
   formar um triângulo.
'''
print('-=' * 13)
print('Analisador de Triângulos')
print('-=' * 13)
a = float(input('Informe o comprimento da primeira reta em metros(m): '))
b = float(input('Informe o comprimento da segunda reta em metros(m): '))
c = float(input('Informe o comprimento da terceira reta em metros(m): '))
if a < b + c and b < a + c and c < a + b:
    print('As retas informadas PODEM formar um triângulo!')
else:
    print('As retas informadas NÃO PODEM formar um triângulo!')







