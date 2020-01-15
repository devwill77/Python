'''
 - DESAFIO 065
 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
   os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
   a digitar valores.
'''
resp = 'S'
soma = cont = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Informe um número inteiro qualquer: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
media = soma / cont
print('Foram informados {} números e a média entre todos os valores informados foi {}'.format(cont, media))
print('O maior número informado foi {} e o menor foi {}'.format(maior, menor))




