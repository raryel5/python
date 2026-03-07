num=str(input('Digite um número: '))
if len(num) == 1:
    num = '000'+num
if len(num) == 2:
    num = '00'+num
if len(num) == 3:
    num = '0'+num

print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))
