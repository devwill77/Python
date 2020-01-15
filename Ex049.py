'''
 - DESAFIO 049
 - Refaça o desafio 009 mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''
num = int(input('Informe o número da tabuada que você deseja ver: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))





