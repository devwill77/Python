'''
 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo desconsiderando os espaços.

'''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
# inverso = junto[::-1] (SOLUÇÃO SEM O USO DO LAÇO DE REPETIÇÃO FOR)
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')










