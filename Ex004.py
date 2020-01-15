
'''
- DESAFIO 004
-Faça um programa que leia algo pelo teclado e mostre na tela
o seu tipo primitivo e todas as informações sobre ele.
'''

algo = input('\033[1;34mDigite algo:\033[m ')
print('\033[30mO tipo primitivo desse valor é\033[m', type(algo))
print('\033[31mSó tem espaços?\033[m', algo.isspace())
print('\033[32mÉ um número?\033[m', algo.isnumeric())
print('\033[33mÉ afabético?\033[m', algo.isalpha())
print('\033[34mÉ alfanumérico?\033[m ', algo.isalnum())
print('\033[35mEstá em maiúsculas?\033[m', algo.isupper() )
print('\033[36mEstá em minúsculas?\033[m ', algo.islower())
print('\033[37mEstá capitalizada?\033[m ', algo.istitle())



