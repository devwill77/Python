'''
- DESAFIO 022
- Crie um programa que leia o nome completo de uma pessoa e mostre:
    - O nome com todas as letras maiúsculas e minúsculas.
    - Quantas letras ao todo (sem considerar espaços).
    - Quantas letras tem o primeiro nome.
'''
nome = str(input('Digite o nome completo de uma pessoa: ')).strip()
print('O nome em maiúsculas é {}'.format(nome.upper()))
print('O nome em minúsculas é {}'.format(nome.lower()))
print('O nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {} letras'.format(nome.find(' ')))

