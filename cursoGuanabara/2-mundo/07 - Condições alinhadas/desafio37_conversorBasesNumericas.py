n = int(input('Digite um número inteiro: '))
print('''Escolha umas das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')

option = int(input('Sua opção: '))
if option == 1:
    print('{} convertido para binário é igual a {}.'.format(n, bin(n)[2:]))
elif option == 2:
    print('{} convertido para octal é igual a {}.'.format(n, oct(n)[2:]))
elif option == 3:
    print('{} convertido para hexadecimal é igual a {}.'.format(n, hex(n)[2:]))
else:
    print('Opção inválida, tente novamente.')
