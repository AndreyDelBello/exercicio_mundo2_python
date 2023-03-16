n = 0
cont = 0
soma = 0
# Ou poderia ser feito n = cont = soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    soma = soma + n
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
    