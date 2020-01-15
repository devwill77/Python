'''
 - DESAFIO 029
 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h mostre uma mensagem
 dizendo que ele foi multado. A multa vai custar R$ 7.00 por cada Km acima do limite.

'''
vel = float(input('Informe a velocidade do carro:  '))
if vel > 80:
    print('Você foi multado por exceder o limite de velocidade que é de 80Km/h!')
    multa = (vel - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia, dirija com segurança!')




