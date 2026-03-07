d=int(input('Quantos quilometros o carro andou? '))
t=int(input('Por quantos dias você ficou com o carro? '))
print('Você ficou {} dias com o carro e andou {}Km, portanto deve pagar R${}.'.format(t, d, (t*60)+(d*0.15)))
