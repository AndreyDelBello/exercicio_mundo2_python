import math
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2
nota = round(media, 1)
print(f'Tirando {n1} e {n2}, a média do aluno é {nota}')

if nota < 5.0:
    print('O aluno está REPROVADO!')
elif nota > 5.0 and nota < 6.9:
    print('O aluno está de RECUPERAÇÃO!')
else:
    print('O aluno está APROVADO!')