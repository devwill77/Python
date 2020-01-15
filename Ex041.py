'''
 - DESAFIO 041
 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
   e mostre sua categoria de acordo com a idade:
   - Até 9 anos: MIRIM
   - Até 14 anos: INFANTIL
   - Até 19 anos: JUNIOR
   - Até 25 anos: SÊNIOR
   - Acima: MASTER
'''
from datetime import date
atual = date.today().year
nasc = int(input('Informe o ano de nascimento do atleta: '))
idade = atual - nasc
print('O atleta está com {} ano(s).'.format(idade))
if idade <= 9:
    print('Este atleta se encaixa na categoria MIRIM.')
elif idade <= 14:
    print('Este atleta se encaixa na categoria INFANTIL.')
elif idade <= 19:
    print('Este atleta se encaixa na categoria JUNIOR.')
elif idade <= 25:
    print('Este atleta se encaixa na categoria SÊNIOR')
else:
    print('Este atleta se encaixa na categoria MASTER')




