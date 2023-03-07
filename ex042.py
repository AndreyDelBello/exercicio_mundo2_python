print("-="*20)
print('Analisador de Triângulos')
print("-="*20)

c1 = float(input('Digite o primeiro segmento: '))
c2 = float(input('Digite o segundo segmento: '))
c3 = float(input('Digite o terceiro segmento: '))

if (c1 + c2) > c3 and (c1 + c3) > c2 and (c2 + c3) > c1:
    if c1 == c2 == c3:
        print('Os segmentos acima PODEM formar um triângulo EQUILATERO!')
    elif c1 == c2 != c3 or c1 == c3 != c2 or c1 != c2 == c3:
        print('Os segmentos acima PODEM formar um triângulo ISÓSCELES!')
    elif c1 != c2 != c3:
        print('Os segmentos acima PODEM formar um triângulo ESCALENO!')
else:
    print('Os segmentos acima NÃO formam um TRIÂNGULO!')
    