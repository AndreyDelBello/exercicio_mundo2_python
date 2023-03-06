from datetime import date
atual = date.today().year
ano = int(input('Informe o ano de nascimento: '))

calc_idade = atual - ano
print('=='*20)
print(f'Quem nasceu em {ano} tem {calc_idade} anos em 2023.')

if calc_idade < 18:
    falta = 18 - calc_idade
    print(f'''Ainda faltam {falta} anos para o alistamento.
Seu alistamento será em {atual+falta}.''')
    print('=='*20)
    
elif calc_idade > 18:
    falta = calc_idade - 18
    print(f'''Você ja deveria ter se alistado há {falta} anos.
Seu alistamento foi em {atual-falta}.''')
    print('=='*20)
    
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
    