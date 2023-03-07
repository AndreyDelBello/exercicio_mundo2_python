import time
from random import randint

print('Suas opções:')
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
e = int(input('Qual é sua jogada? '))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('POO!!!')
time.sleep(1)
maquina = randint(1, 3)

# OUTPUT MAQUINA
print('-='*10)
if maquina == 1:
    print(f'Computador jogou Pedra')
elif maquina == 2:
    print(f'Computador jogou Papel')
elif maquina == 3:
    print(f'Computador jogou Tesoura')
    
# OUTPUT JOGADOR
if e == 1:
    print(f'Jogador jogou Pedra')
elif e == 2:
    print(f'Jogador jogou Papel')
elif e == 3:
    print(f'Jogador jogou Pesoura')
print('-='*10)

###===================================================
#LOGICA DO GAME

if maquina == 1 and e == 2:
    print('VOCÊ GANHOU!')
elif maquina == 2 and e == 3:
    print('VOCÊ GANHOU!')
elif maquina == 3 and e == 1:
    print('VOCÊ GANHOU!')
elif e == 1 and maquina == 2:
    print('COMPUTADOR VENCEU!')
elif e == 2 and maquina == 3:
    print('COMPUTADOR VENCEU!')
elif e == 3 and maquina == 1:
    print('COMPUTADOR VENCEU!')
else:
    print('EMPATOU!')
    
