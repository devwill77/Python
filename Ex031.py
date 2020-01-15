'''
 - DESAFIO 031
 - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem cobrando
 R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas.
'''
distância = float(input('informe a distância da viagem em Km: '))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('Sua viagem será de {}Km e custará R${:.2f}'.format(distância, preço))

'''
Obs:
Estrutura condicional de forma simplificada
preço = distância * 0.50 if <= 200 else distância * 0.45
'''








