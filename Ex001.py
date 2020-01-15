'''
DESAFIO 01
- Crie um script Python que leia o nome de uma pessoa e mostre
uma mensagem de boas vindas de acordo com o valor digitado.
'''
nome = str(input('\033[36mQual o seu nome?\033[m '))

print('\033[31mOlá\033[m {}{}{}\033[31m, muito prazer em te conhecer!\033[m'.format('\033[1;34m', nome, '\033[m'))






