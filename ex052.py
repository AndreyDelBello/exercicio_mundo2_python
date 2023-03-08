num = int(input('Digite um numero: '))
mult = 0

for count in range(1, num+1, 1):
    print(count, end=' ')
    if (num % count == 0):
        print(f'O numero {num} foi dividisivel 2 vezes')
        print(f'E por isso ele É PRIMO!')