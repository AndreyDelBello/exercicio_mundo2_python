#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
#que ele conquistou no final do jogo.

from random import randint

vitoriaJ = 0
while True:
    pc  = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    parimpar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]  
    
    if parimpar == 'P' and (jogador + pc) % 2 == 0:
        print(f'Você jogou {jogador} e o computador {pc}. Total de {pc+jogador} deu PAR.')
        vitoriaJ +=1
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-'*30)
        
    elif parimpar == 'I' and (jogador + pc) % 2 != 0:
        print(f'Você jogou {jogador} e o computador {pc}. Total de {pc+jogador} deu ÍMPAR.')
        vitoriaJ +=1
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-'*30)
        
    else:
        print(f'Você jogou {jogador} e o computador {pc}. Total de {pc+jogador} deu ÍMPAR.')
        print('='*20)
        print('Você PERDEU!')
        print('=-'*30)
        print(f'GAME OVER! Você venceu {vitoriaJ} vezes.')
        break

