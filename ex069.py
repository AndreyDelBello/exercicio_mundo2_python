contpessoas = 0
demaior = 0
homem = 0
mulhermenor = 0

while True:
    print("--"*10)
    print("CADASTRE UMA PESSOA")
    print("--"*10)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    contpessoas += 1
    if idade > 18:
        demaior += 1
    if sexo == 'M' and idade < 100:
        homem += 1
    if sexo == 'F' and idade < 20:
        mulhermenor += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] -> ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Foram cadastradas {contpessoas} pessoas.')
print(f'Total de pessoas com mais de 18 anos: {demaior}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulhermenor} mulheres com menos de 20 anos')
    
    

    