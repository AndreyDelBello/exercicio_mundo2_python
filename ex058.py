from random import randint
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
p = int(input('Qual é seu palpite? '))
pc = randint(0, 10)
contvezes = 0

while p != pc:
    if pc > p:
        print('Mais... Tente mais uma vez.')
        p = int(input('Qual é seu palpite? '))
        contvezes += 1
    else:
        print('Menos... Tente mais uma vez.')
        p = int(input('Qual é seu palpite? '))
        contvezes += 1
contvezes += 1
print(f'Acertou com {contvezes} tentativas. Parabéns!')
