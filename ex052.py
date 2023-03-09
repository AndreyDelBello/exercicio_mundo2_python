num = int(input('Digite um numero: '))
total = 0

for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO numero {num} foi divisivel {total} vezes.')
if total == 2:
    print(f'Então {num} é um número primo.')
else:
    print(f'Então {num} não é um número primo.')
