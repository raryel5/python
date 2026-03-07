a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
if a < b+c and b < a+c and c < a+b:
    print('Esses segmentos formam um triângulo.')
else:
    print('Os segmmentos não formam um triângulo.')
