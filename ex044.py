print('='*16,'LOJAS ANDREY','='*16)
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartao')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    novo_preco = preco - (preco * (10/100))
    print(f'Sua compra de R${preco} vai custar r${novo_preco:.2f} no final.')
elif opcao == 2:
    novo_preco = preco - (preco * (5/100))
    print(f'Sua compra de R${preco} vai custar r${novo_preco:.2f} no final.')
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} totalizando R${preco:.2f} SEM JUROS')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = (preco * 0.20 * parcelas) / parcelas
    parcela_juros = (preco + juros) / parcelas
    preco_total = preco + juros
    print(f'Sua compra parcelada em {parcelas}x de R${parcela_juros:.2f} COM JUROS')
    print(f'Sua compra de R${preco:.2f} vai custar R${preco_total:.2f} no final.')
else:
    print('Operação invalida. Tente novamente.')
