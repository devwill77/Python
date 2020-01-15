'''
- DESAFIO 010
- Crie um programa que leia quanto dinheiro uma pessoa
tem na carteira e mostre quantos dólares ela pode comprar.
Considere
U$$1.00 = R$3.27
'''
grana = float(input('Quanto dinheiro vc tem na carteira? R$'))
dolar = grana / 4.26
euro = grana / 4.69
print('Com R${:.2f} vc pode comprar US${:.2f} e {:.2f} euros'.format(grana, dolar, euro))





