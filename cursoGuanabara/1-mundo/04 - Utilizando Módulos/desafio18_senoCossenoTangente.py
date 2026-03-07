from math import sin, radians, cos, tan
ang = radians(float(input('Digite um ângulo: ')))
seno = sin(ang)
cosseno = cos(ang)
tangente = tan(ang)
print('O seno de {:.2f}rad vale {:.2f}'.format(ang, seno))
print('Seu cosseno vale {:.2f}'.format(cosseno))
print('A sua tangente vale {:.2f}'.format(tangente))


