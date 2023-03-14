r = 'MF'
n = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

while n not in 'MmFf':
    n = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {n} registrado com sucesso! ')
    
    