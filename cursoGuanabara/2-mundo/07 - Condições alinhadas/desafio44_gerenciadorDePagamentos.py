valor = float(input('Qual é o valor da sua compra? R$'))
a = int(1)
while a != 0:
    print('\033[1;31;40m ===== MARLON EMPREENDIMENTOS ===== \033[m')
    print('[ 1 ] à vista dinheiro/cheque;')
    print('[ 2 ] à vista cartão;')
    print('[ 3 ] 2x no cartão;')
    print('[ 4 ] 3x ou mais no cartão;')
    print('[ 0 ] finalizar compra;')
    option = int(input('\033[1;33;40m Qual a forma de pagamento? \033[m'))
    if option == 1:
        print('Sua compra de R${} vai custar R${} pagando a vista no dinheiro ou cheque.'.format(valor, valor*0.9))
        b = input('Deseja fazer colsultar outra forma de pagamento? s/n: ')
        if b == 's':
            a = 1
        else:
            a = 0
            print('Obrigado pela compra.')
    elif option == 2:
        print('Sua compra de R${} vai custar R${} pagando a vista no cartão.'.format(valor, valor*0.95))
        b = input('Deseja fazer colsultar outra forma de pagamento? s/n: ')
        if b == 's':
            a = 1
        else:
            a = 0
            print('Obrigado pela compra.')
    elif option == 3:
        vpar = valor/2
        print('Sua compra de R${} vai custar R${} pagando em 2x de R${} no cartão.'.format(valor, valor, vpar))
        b = input('Deseja fazer colsultar outra forma de pagamento? s/n: ')
        if b == 's':
            a = 1
        else:
            a = 0
            print('Obrigado pela compra.')
    elif option == 4:
        par = int(input('Em quantas parcelas você quer pagar? '))
        vpar = valor/par
        print('Sua compra de R${} vai custar R${} pagando em {}x de R${} no cartão.'.format(valor, 1.2*valor, par, vpar))
        b = input('Deseja fazer colsultar outra forma de pagamento? s/n: ')
        if b == 's':
            a = 1
        else:
            a = 0
            print('Obrigado pela compra.')
    elif option == 0:
        a=0
        print('Obrigado pela compra.')
