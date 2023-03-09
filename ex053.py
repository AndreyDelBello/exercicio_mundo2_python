frase = str(input('Digite uma frase: ')).strip().upper()
juntar = frase.replace(" ", "")

print(f'O inverso de {juntar} é {juntar[::-1]} ')

if juntar[::-1] == juntar:
    print('Temos um palindromo!')
else:
    print('Esta frase nao é um palindromo.')