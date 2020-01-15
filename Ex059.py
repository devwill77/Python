'''
 - DESAFIO 059
 - Crie um programa que leia dois valores e mostre um menu como ao lado na tela:     [1]somar
                                                                                     [2]multiplicar
                                                                                     [3]maior
                                                                                     [4]novos números
                                                                                     [5]sair do programa
   Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep
valor1 = int(input('Informe o primeiro número inteiro: '))
valor2 = int(input('Informe o segundo número inteiro: '))
op = 0
while op != 5:
    print('''    [ 1 ] -> Somar
    [ 2 ] -> Multiplicar
    [ 3 ] -> Maior
    [ 4 ] -> Novos números
    [ 5 ] -> Sair do Programa''')
    op = int(input('>>>>>> O que deseja fazer? (Escolha uma das opções acima): '))
    if op == 1:
        soma = valor1 + valor2
        print('O resultado de {} + {} é {}.'.format(valor1, valor2, soma))
    elif op == 2:
        multiplica = valor1 * valor2
        print('O resultado de {} x {} é {}.'.format(valor1, valor2, multiplica))
    elif op == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('Entre os números {} e {} o maior deles é o {}.'.format(valor1, valor2, maior))
    elif op == 4:
        print('Informe os novos números')
        valor1 = int(input('Informe o primeiro número inteiro: '))
        valor2 = int(input('Informe o segundo número inteiro: '))
    elif op == 5:
        print('Finalizando.............')
    else:
        print('Opção inválida. Tente novamente!')
    print('=' * 25)
    sleep(2)
print('<<<< FIM DO PROGRAMA!!! >>>>')

















