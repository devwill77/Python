'''
 - DESAFIO 050
 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
   que forem pares. Se o valor digitado for ímpar desconsidere - o.
'''
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Informe o {}° número inteiro: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Foram informados {} número(s) par(es) e o resultado da soma do(s) mesmo(s)  é igual a {}.'.format(cont, soma))













