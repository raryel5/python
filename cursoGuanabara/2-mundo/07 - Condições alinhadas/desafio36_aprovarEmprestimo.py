val = float(input('Qual é o valor da casa? '))
sal = float(input('Qual é o seu salário? '))
ano = int(input('Em quantos anos você quer pagar? '))
prestacao = val/(12*ano)
if prestacao <= (0.3*sal):
    print('Para você conseguir pagar em {} anos, a prestação mensal será de R${:.2f}.'.format(ano, prestacao))
else:
    print('Desista, você não pode pagar essa casa ganhando essa merreca de salário!')
    
