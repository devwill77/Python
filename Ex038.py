'''
 - DESAFIO 038
 - Escreva um programa que leia dois números inteiros e compare - os mostrando na tela uma
   mensagem:
   - O primeiro valor é maior
   - O segundo valor é maior
   - Não existe valor maior, os dois são iguais
'''
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
if num1 > num2:
    print('O \033[1;31mPRIMEIRO\033[m valor é \033[1;36mMAIOR\033[m')
elif num2 > num1:
    print('O \033[1;31mSEGUNDO\033[m valor é \033[1;36mMAIOR\033[m')
else:
    print('Não existe valor maior, os dois valores são \033[1;34mIGUAIS\033[m')











