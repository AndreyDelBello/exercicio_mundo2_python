from time import sleep

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
r = 0
while r != 5:
    print('''    [ 1 ] Somar
    [ 2 ] multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa''')
    r = int(input('Qual é a sua opção? '))

    if r == 1:
        print(f'A soma entre {v1} + {v2} é {v1+v2}')
        print('=-'*20)
        sleep(2)
    elif r == 2:
        print(f'A multiplicação entre {v1} x {v2} é {v1*v2}')
        print('=-'*20)
        sleep(2)
    elif r == 3:
        lista = [v1, v2]
        print(f'Entre {v1} e {v2} o maior é {max(lista)}')
        print('=-'*20)
        sleep(2)
    elif r == 4:
        print('Informe os números novamente: ')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
        print('=-'*20)
        sleep(2)
    elif r != 1 and r != 2 and r != 3 and r != 4 and r != 5:
        print('Operação inválida. Tente novamente')
        print('=-'*20)
        sleep(2)

print('Finalizando...')
sleep(2)
print('Fim do programa! Volte Sempre!')
        
