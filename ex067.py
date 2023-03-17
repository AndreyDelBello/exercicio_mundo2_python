# Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

n = 1

while n > 0:
    print('='* 30)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('='* 30)
        
    if n < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')
        break
    
    c = 0
    while c < 10:
        print(f'{n} x {c} = {n*c}')
        c += 1
        
    

