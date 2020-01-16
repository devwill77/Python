'''
 - DESAFIO 069
 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
   perguntar se o usuário quer ou não continuar. No final mostre:
   A - Quantas pessoas tem mais de 18 anos.
   B - Quantos homens foram cadastrados.
   C - Quantas mulheres tem menos de 20 anos
'''
tot18 = tot_homem = tot_mulher = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tot_homem += 1
    if sexo == 'F' and idade < 20:
        tot_mulher += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens cadastrados: {tot_homem}')
print(f'Total de mulheres com menos de 20 anos: {tot_mulher}')
print('Acabou!')




