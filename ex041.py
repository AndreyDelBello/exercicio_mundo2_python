from datetime import date
atual = date.today().year
ano = int(input('Informe o ano de nascimento: '))

idade = atual - ano
print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação: JÚNIOR')
elif idade > 19 and idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')