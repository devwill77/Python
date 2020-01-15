'''
 - DESAFIO 044
 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
   condição de pagamento:
   - á vista dinheiro/cheque: 10% de desconto
   - à vista no cartão: 5% de desconto
   - em até 2x no cartão: preço normal
   - 3x ou mais no cartão: 20% de juros
'''
print('\033[1;34m{:=^40}\033[m'.format(' MAGAZINE SANTOS '))
preço = float(input('\033[1;32mInforme o preço do produto: R$\033[m'))
op = int(input('''
\033[7;30mESCOLHA SUA OPÇÃO:\033[m
\033[33m[1] - á vista em dinheiro/Cheque\033[m
\033[33m[2] - á vista no cartão\033[m
\033[33m[3] - até 2x no cartão\033[m
\033[33m[4] - até 3x ou mais no cartão\033[m '''))
if op == 1:
    total = preço - (preço * 10 / 100)
elif op == 2:
    total = preço - (preço * 5 / 100)
elif op == 3:
    total = preço
    parcela = preço / 2
    print('\033[36mSeu produto será dividido em 2x de R${:.2f} s/juros\033[m'.format(parcela))
elif op == 4:
    total = preço + preço * 20 / 100
    totalparcelas = int(input('\033[33mInforme o n° de parcelas: \033[m'))
    parcela = total / totalparcelas
    print('\033[36mSeu produto será dividido em {}x de R${:.2f} c/juros\033[m'.format(totalparcelas, parcela))
else:
    total = preço
    print('\033[1;31mOPÇÃO INVÁLIDA, tente novamente!\033[m')
print('\033[34mO produto que custa R${:.2f} vai custar R${:.2f}\033[m'.format(preço,total))








