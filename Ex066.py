'''
 - DESAFIO 066
 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
   digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e
   qual foi a soma entre eles (desconsiderando o Flag).
'''
cont = soma = 0
while True:
    n = int(input('Digite um número inteiro [Para sair do programa digite 999]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Foram digitados {cont} números e a soma entre eles foi {soma}')


