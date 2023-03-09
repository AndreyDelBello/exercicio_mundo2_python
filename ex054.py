from datetime import date
totpessoas = 0
totpessoasmenores = 0
atual = date.today().year

for c in range(1, 8):
    p = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    idade = atual - p
    if idade >= 18:
        totpessoas += 1
    else:
        totpessoasmenores += 1

print(f'Ao todo tivemos {totpessoas} pessoas maiores de idade.')
print(f'E também tivemos {totpessoasmenores} pessoas menores de idade.')
    