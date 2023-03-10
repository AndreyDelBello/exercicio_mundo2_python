lista = []

for c in range(1, 6):
    peso = float(input(f'Qual é o peso da {c} pessoa? '))
    lista.append(peso)
    
print(f'Teste de peso das pessoas: {lista}')
print(f'O peso maior lido foi de {max(lista)}Kg.')
print(f'O peso menor lido foi de {min(lista)}Kg.')

        
