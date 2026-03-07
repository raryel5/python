from math import sqrt
l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))
#print('\033[4;33;47m')

if ((l1 + l2) < l3) or ((l1 + l3) < l2) or ((l2 + l3) < l1):
    print('\033[1;31;40m Esses valores não formam qualquer triângulo.')

elif (l1 == sqrt((l2**2)+(l3**2))) or (l2 == sqrt((l1**2)+(l3**2))) or (l3 == sqrt((l2**2)+(l1**2))):
    print('\033[4;34;40m {}, {} e {} formam um triângulo RETÂNGULO.'.format(l1, l2, l3))

elif l1 == l2 and l1 == l3:
    print('{}, {} e {} formam um triângulo EQUILÁTERO.'.format(l1, l2, l3))

elif l1 == l2 or l1 == l3 or l2 == l3:
    print('{}, {} e {} formam um triângulo ISÓCELES.'.format(l1, l2, l3))

elif l1 != l2 and l1 != l3:
    print('{}, {} e {} formam um triângulo ESCALENO.'.format(l1, l2, l3))

print('\033[m')

