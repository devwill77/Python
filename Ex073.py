'''
 - DESAFIO 073
 - Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol na ordem
   de colocação. Depois mostre:
   A - os 5 primeiros.
   B - Os últimos 4 colocados.
   C - Times em ordem alfabética.
   D - Em que posição está o time do Chapecoense.
'''
times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio',
         'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians',
         'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama',
         'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará SC',
         'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('+' * 100)
print(f'Lista de times do Brasileirão -> {times}')
print('+' * 100)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('+' * 100)
print(f'Os últimos 4 colocados são: {times[-4:]}')
print('+' * 100)
print(f'Organizado em ordem alfabética a lista dos times fica a seguinte -> {sorted(times)}')
print('+' * 100)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição da lista.')


















