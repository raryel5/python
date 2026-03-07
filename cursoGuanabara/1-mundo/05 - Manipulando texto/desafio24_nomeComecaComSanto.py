nome = input('Digite um nome de cidade: ')
a = nome.split()
if a[0] == 'SANTO':
    print('O nome da cidade {} começa com SANTO'.format(nome))
else:
    print('A cidade {} não começa com a palavra SANTO'.format(nome))
