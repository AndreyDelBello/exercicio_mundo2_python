soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite algum numero inteiro: '))
    if num % 2 == 0:
        cont += 1
        soma += num
print(f'Você informou {cont} numeros PARES e a soma foi de {soma}')