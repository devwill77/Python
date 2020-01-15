'''
- DESAFIO 013
- Faça um algoritmo que leia o salario de um funcionário e mostre
seu novo salário com 15% de aumento.
'''
salario = float(input('Informe o salário do funcionário: R$'))
novo_salario = salario + (salario * 15 / 100)
print('O funcionário que ganhava {:.2f} com 15% de aumento passará a receber {:.2f}'.format(salario, novo_salario))
