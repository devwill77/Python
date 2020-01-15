'''
 - DESAFIO 039
 - Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade se ele
   ainda vai se alistar no serviço militar, se é a hora de se alistar ou se já passou do tempo do
   alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
nasc = int(input('informe o ano que você nasceu: '))
sexo = str(input('''Informe seu sexo:
Digite \033[34m(m)\033[m para masculino e \033[35m(f)\033[m para feminino)
'''))

atual = date.today().year
idade = atual - nasc
if sexo == 'm':
    if idade < 18:
        saldo = 18 - idade
        print('\033[1;34mVocê está com {} ano(s), ou seja, falta(m) {} ano(s) para seu alistamento!\033[m'.format(idade, saldo))
        ano = atual + saldo
        print('\033[1;36mSeu alistamento será no ano de {}.\033[m'.format(ano))
    elif idade == 18:
        print('\033[1;34mVocê está com {} ano(s), ou seja, deverá se alistar IMEDIATAMENTE!!!\033[m'.format(idade))
    elif idade > 18:
        saldo = idade - 18
        print('\033[1;34mVocê está com {} ano(s), ou seja, você deveria ter se alistado há {} ano(s).\033[m'.format(idade, saldo))
        ano = atual - saldo
        print('\033[1;36mSeu alistamento foi no ano de {}.\033[m'.format(ano))
elif sexo == 'f':
    print('\033[1;34mVocê não precisará fazer o alistamento militar obrigatório!!!\033[m')
else:
    print('\033[1;31mOpção inválida, tente novamente por favor!\033[m')












