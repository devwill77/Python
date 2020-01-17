'''
 - DESAFIO 070
 - Crie um programa que leia o nome e o preço de vários produtos. o programa deverá perguntar se o
   usuário vai continuar. No final mostre:
   A - Qual é o total gasto na compra
   B - Quantos produtos custam mais de R$1000,00
   C - Qual é o nome do produto mais barato.
'''
# Título do programa
nm_loja = 'KI BARATO'
print(f'{nm_loja:#^60}')
total = acima_mil = menor = cont = 0 #Variáveis de controle e auxiliares
nm_produto_mbarato = ''
# Laço responsável por solicitar várias vezes os dados para o usuário
while True:
    nm_produto = str(input('Informe o nome do produto: ')) # Solicita o nome do produto
    preço_produto = float(input('Informe o preço do produto: R$')) # Solicita o preço do produto
    cont += 1 # Contador responsável por contar a quantidade de produtos
    total += preço_produto  # Acumulador que irá fazer um somatório do valor de todos os produtos
    if preço_produto > 1000:# Parte que mostra a quantidade de produtos acima de R$1000,00
        acima_mil += 1
    if cont == 1 or preço_produto < menor:
        menor = preço_produto #Parte que determina o nome e preço do produto mais barato
        nm_produto_mbarato = nm_produto
    resp = ' '
    while resp not in 'SN': # parte que valida se o usuário quer continuar ou não no programa
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Valor total da compra: R${total:.2f}')
print(f'Quantidade de produtos que custam mais de R$1000,00: {acima_mil}')
print(f'O produto mais barato foi {nm_produto_mbarato} que custa {menor:.2f}')

print('{:-^40}'.format('FIM DO PROGRAMA'))








