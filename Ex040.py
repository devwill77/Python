'''
 - DESAFIO 040
 - Crie um programa que leia duas notas de um aluno  e calcule sua média mostrando uma mensagem no final
   de acordo com a média atingida:
   - Média abaixo de 5.0: REPROVADO
   - Média entre 5.0 e 6.9: RECUPERAÇÃO
   - Média 7.0 ou superior: APROVADO
'''
n1 = float(input('Informe a primeira nota do aluno : '))
n2 = float(input('Informe a segunda nota do aluno :'))
média = (n1 + n2) / 2
print('A média entre as notas {:.1f} e {:.1f} é igual a {:.1f}.'.format(n1, n2, média))
if média < 5:
    print('Você foi REPROVADO!')
elif média >= 5 and média < 7:
    print('Cuidado, você ficou de RECUPERAÇÃO!')
elif média >= 7:
    print('Parabéns, você foi APROVADO!!!')





