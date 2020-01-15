'''
 - DESAFIO 043
 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre o seu status
   de acordo com a tabela abaixo:
   - Abaixo de 18.5: Abaixo do peso
   - Entre 18.5 e 25: Peso ideal
   - 25 até 30: Sobrepeso
   - 30 até 40: Obesidade
   - Acima de 40: Obesidade mórbida
'''
peso = float(input('informe o peso do indivíduo em quilogramas(Kg): '))
altura = float(input('Informe a altura do indivíduo em metros(m): '))
imc = peso / altura**2
print('De acordo com os valores informados o IMC é igual a {:.2f}, ou seja, é classificado como '.format(imc), end='')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc <= 25:
    print('PESO IDEAL')
elif imc <= 30:
    print('SOBREPESO')
elif imc <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')





