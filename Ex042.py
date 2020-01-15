'''
 - DESAFIO 042
 - Refaça o desafio 035 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado:
 - Equilátero: Todos os lados iguais
 - Isósceles: Dois lados iguais
 - Escaleno: Todos os lados diferentes
'''
print('-=' * 13)
print('Analisador de Triângulos v 2.0')
print('-=' * 13)
a = float(input('Informe o comprimento da primeira reta em metros(m): '))
b = float(input('Informe o comprimento da segunda reta em metros(m): '))
c = float(input('Informe o comprimento da terceira reta em metros(m): '))
if a < b + c and b < a + c and c < a + b:
    print('As retas informadas PODEM formar um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO!')
    elif a != b != c != a:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('As retas informadas NÃO PODEM formar um triângulo!')
