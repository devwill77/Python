'''
 - DESAFIO 034
 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
 Para salários superiores a R$1250.00 calcule um aumento de 10%.
 Para os inferiores ou iguais o aumento é de 15%.
'''
salário = float(input('Informe o salário atual do funcionário: R$'))
if salário <= 1250:
    novo_salário = salário + (salário * 15 / 100)
else:
    novo_salário = salário + (salário * 10 / 100)

print('O salário atual do funcionário de R${:.2f} com o aumento passará a ser de R${:.2f}'.format(salário, novo_salário))











