
'''
- DESAFIO 005
- Faça um programa que leia um número inteiro e mostre
o seu sucessor e seu antecessor
'''

num = int(input('\033[35mDigite um número inteiro qualquer:\033[m '))

print('\033[32mO número digitado foi \033[34m{}\033[m\033[32m, seu sucessor é'
      '\033[m \033[31m{}\033[m \033[32me seu antecessor é\033[m \033[36m{}\033[m'.format(num, num + 1, num - 1))

