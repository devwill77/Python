'''
 - DESAFIO 056
 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
  - A média de idade do grupo.
  - Qual é o nome do homem mais velho.
  - Quantas mulheres tem menos de 20 anos
'''
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
totmulher20 = 0
for pessoa in range(1, 5):
    print('----- {}ª PESSOA -----'.format(pessoa))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]:')).strip()
    soma_idade += idade
    if pessoa == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
media_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos.'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nome_mais_velho))
print('No total há {} mulher(es) com menos de 20 anos.'.format(totmulher20))
















