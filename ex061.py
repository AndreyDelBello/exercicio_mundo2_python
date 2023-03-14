print('='* 20)
print('Gerador de PA')
print('='* 20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
while cont <= 10:
    if cont < 10:
        print(f'{primeiro} --> ', end='')
    elif cont == 10:
        print(f'{primeiro}', end='')
    primeiro += razao
    cont += 1
print('--> FIM')
