'''
 - DESAFIO 072
 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte.
   Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá - lo por extenso.
'''
cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    num = int(input('Informe um número entre 0 e 20: '))
    if num < 0 or num > 20:
        print('Tente novamente!')
    else:
        print(f'O número informado foi o {cont[num]}')
        resp = ' '
        while resp not in 'SN':
            resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if resp == 'N':
            break
print('Obrigado e volte sempre!')






















