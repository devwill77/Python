'''
 - DESAFIO 032
 - Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

'''
from datetime import date # Biblioteca que importa funcionalidades de data...

ano = int(input('informe um ano qualquer e se quiser analisar o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year # Pega o ano atual configurado na máquina

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO.'.format(ano))




