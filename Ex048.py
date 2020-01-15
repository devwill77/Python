'''
 - DESAFIO 048
 - Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
   encontram no intervalo de 1 até 500.
'''
cont = 0
soma = 0
for n in range(1, 500, 2):
    if n % 3 == 0:
        cont += 1
        soma += n
print('A soma dos {} valores é igual a {}'.format(cont, soma))






