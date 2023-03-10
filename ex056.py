lista = []
contmulher = 0

for c in range(1, 5):
    print(f'----- {c}º PESSOA -----')
    nome = str(input(f'Nome: '))
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M/F]: ')).upper()
    lista.append(idade)
    if sexo == 'M':
        idadeH = max(lista)
        
    elif sexo == 'F' and idade < 20: # contagem das mulheres com menos de 20 anos.
        contmulher += 1
    
media = sum(lista) / 4 # Média de idade do grupo.

print(f'A média de idade do grupo é de {media:.1f} anos.')
print(f'O homem mais velho tem {idadeH} anos.')
print(f'Ao todo são {contmulher} mulheres com menos de 20 anos.')



