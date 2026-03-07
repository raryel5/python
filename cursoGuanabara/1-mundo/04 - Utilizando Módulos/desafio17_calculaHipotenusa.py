from math import hypot
print('\n' *20)
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
#hi = (co**2 + ca**2)**(0.5)
print('A hipotenusa desse triâncgulo vale {:.2f}'.format(hypot(co, ca)))
