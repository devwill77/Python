'''
 - DESAFIO 071
 - Crie um programa que simule o funcionamento de um caixa eletrônico. No início pergunte ao usuário qual será
   o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
   Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
print('=' * 100)
print('{:^100}'.format('BANCO WS LIMA'))
print('=' * 100)
print('''CÉDULAS DISPONÍVEIS:
50
20
10
1''')
print('+' * 100)
valor = int(input('Saudações meu caro amigo(a), qual o valor que deseja sacar hoje? R$'))
total = valor
cédula = 50
totcédula = 0
while True:
    if total >= cédula:
        total -= cédula
        totcédula +=1
    else:
        if totcédula > 0:
            print(f'{totcédula} cédulas de R${cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 5
        elif cédula ==5:
            cédula = 1
        totcédula = 0
        if total == 0:
            break
print('+' * 100)
print('Agradecemos por sua preferência, muito obrigado e volte sempre!!!!')
print('+' * 100)













