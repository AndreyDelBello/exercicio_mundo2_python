num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL ''')
opcao = int(input('Escolha uma das bases para conversão: '))

if opcao == 1:
    print(f'Sua opção: {opcao}')
    num_binario = bin(num)[2:]
    print(f'{num} convertido para BINARIO é igual a {num_binario}')
    
elif opcao == 2:
    print(f'Sua opção: {opcao}')
    num_octal = oct(num)[2:]
    print(f'{num} convertido para OCTAL é igual a {num_octal}')

elif opcao == 3:
    print(f'Sua opção: {opcao}')
    num_hex = hex(num)[2:]
    print(f'{num} convertido para HEXADECIMAL é igual a {num_hex}')
else:
    print('Operação inválida. Tente Novamente.')
