v = float(input('Qual a velocidade do carro? '))
multa = (v-80)*7
if v > 80:
    print('Acima da velocidade permitida! Multa de R${:.2f}'.format(multa))
else:
    print('Ok, velocidade dentro do limite permitido.')
