r = 'S'
num = 0
cont = 0
soma = 0
lista = []
while r not in 'NAO':
    num = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] -> ')).strip().upper()[0]
    lista.append(num)
    cont += 1
    soma += num
    media = soma / cont
print(f'Você digitou {cont} números e a média foi {media}')
print(f'O amior valor foi {max(lista)} e o menor foi {min(lista)}')
    
    
    
    