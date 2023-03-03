casa = float(input('Qual o valor da casa? '))
salario = float(input('Salário do comprador? '))
ano = int(input('Quantos anos de financiamento? '))

calc = ano * 12
prestacao = (casa / calc) 
print(f'Para pegar uma casa de R${casa:.2f} em {ano} anos a prestação será de R${prestacao:.2f}')

if prestacao > salario*0.30:
    print('Emprestimo NEGADO!')
elif prestacao < salario*0.30:
    print('Emprestimo CONCEDIDO!')
    
