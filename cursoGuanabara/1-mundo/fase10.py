n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.2f}'.format(m))
if m >= 6.0:
    if m<=7:
        print('Parabéns! você está aprovado!')
    elif m>7 and m<=9:
        print('Parabéns! sua média foi ótima!')
    elif m>9:
        print('Parabéns! Sua média foi excelente!')
else:
    print('Infelizmente você não foi aprovado, tente novamente!')
