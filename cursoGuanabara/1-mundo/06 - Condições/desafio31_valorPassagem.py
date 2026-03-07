d = float(input('Qual a distância da sua viagem? '))
if d <= 200:
    print('A distância da sua viagem é menor do que 200km, então o valor da passagem para {}km é de R${:.2f}.'.format(d, (d*0.5)))
else:
    print('A distância da sua viagem é maior do que 200km, então o valor da passagem para {}km é de R${:.2f}.'.format(d, (d*0.45)))
