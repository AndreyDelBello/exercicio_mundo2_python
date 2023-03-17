r = 'S'
contpessoas = 0
demaior = 0
homens = 0
mulhermenor = 0

while r == 'S':
    print("--"*10)
    print("CADASTRE UMA PESSOA")
    print("--"*10)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    contpessoas += 1
    if idade > 18:
        demaior += 1
    elif sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulhermenor += 1
    r = str(input('Quer continuar? [S/N] -> ')).strip().upper()[0]

print(f'Foram cadastradas {contpessoas} pessoas.')
print(f'Total de pessoas com mais de 18 anos: {demaior}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos 1 mulheres com menos de {mulhermenor} anos')
    
    

    