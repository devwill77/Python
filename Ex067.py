'''
 - Faça um programa que mostre a tabuada de vários números, um de cada vez para cada valor digitado
   pelo usuário. o programa será interrompido quando o número solicitado for negativo.
'''
while True:
    num = int(input('Informe o número da tabuada que você deseja visualizar [Caso queira sair digite um número negativo]: '))
    print('-' * 30)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num * c:2}')
    print('-' * 30)
print('\nSaída do programa concluída com sucesso!!!!')


