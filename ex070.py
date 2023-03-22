totcompra = 0
contpreco = 0
menor = 0 
cont =0
barato = ' '

while True:
    print('='*20)
    print('LOJA SUPER BARATÃO')
    print('='*20)

    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    totcompra += preco
    if preco > 1000:
        contpreco += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
        
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        print('='*10, 'FIM DO PROGRAMA', '='*10)
        break

print(f'O total da compra foi R${totcompra:.2f}')
print(f'Temos {contpreco} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi o {barato} que custa {menor:.2f}')