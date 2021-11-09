from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qua é a sua jogada? '))
print('PEDRA')
sleep(0.6)
print('PAPEL')
sleep(0.6)
print('TESOOOURA')
print('~*'*12)
print('Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[jogador]))
print('~*'*12)
if pc == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR WINS')
    elif jogador == 2:
        print('COMPUTADOR WINS')
    else:
        print('Jogada INVÁLIDA')
elif pc == 1:
    if jogador  == 0:
        print('COMPUTADOR WINS')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR WINS')
    else:
        print('Jogada INVÁLIDA')

elif pc == 2:
    if jogador == 0:
        print('JOGADOR WINS')
    elif jogador == 1:
        print('COMPUTADOR WINS')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada INVÁLIDA')