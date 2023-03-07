peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual é a sua altura? '))

imc = peso / (altura * altura)
print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc < 18.5:
    print('Você está está em ABAIXO DE PESO!')
elif imc <= 25:
    print('Você está está em PESO IDEAL!')
elif imc <= 30:
    print('Você está está em SOBREPESO!')
elif imc <= 40:
    print('Você está está em OBESIDADE!')
else:
    print('Você está está em OBESIDADE MÓRBIDA!')
