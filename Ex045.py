'''
 - DESAFIO 045
 - Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randint
from time import  sleep
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print('Quero ver se você consegue me vencer em um joguinho de JOKENPÔ...')
print('''Escolha uma opção:
[0] = PEDRA
[1] = PAPEL
[2] = TESOURA''')
jogador = int(input('Informe a opção escolhida: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('+' *22)
print('Você escolheu {}'.format(itens[jogador]))
print('Eu escolhi {}'.format(itens[computador]))
print('+' * 22)
if jogador == 0:
    if computador == 0:
        print('EMPATOU!!!')
    elif computador == 1:
        print('HAHA, VENCI!!!')
    elif computador == 2:
        print('Oh não, você VENCEU!!!')
    else:
        print('OPÇÃO INVÁLIDA, tente novamente!')
if jogador == 1:
    if computador == 0:
        print('Oh não, você VENCEU!!!')
    elif computador == 1:
        print('EMPATOU!!!')
    elif computador == 2:
        print('HAHA, VENCI!!!')
    else:
        print('OPÇÃO INVÁLIDA, tente novamente!')
if jogador == 2:
    if computador == 0:
        print('HAHA, VENCI!!!')
    elif computador == 1:
        print('Oh não, você VENCEU!!!')
    elif computador == 2:
        print('EMPATOU!!!')
    else:
        print('OPÇÃO INVÁLIDA, tente novamente!')























