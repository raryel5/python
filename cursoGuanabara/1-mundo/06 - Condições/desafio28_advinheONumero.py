import random
x = random.randint(0,5)
chance = int(input('Digite um número entre 0 e 5, e boa sorte! '))
if chance == x:
    print('Que sorte! Você acertou!')
else:
    print('Que pena, você não acertou, mais sorte na próxima.')
    print('O número da sorte foi {}'.format(x))
