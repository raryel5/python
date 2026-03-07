while True:
    a = str(input('Quanto você quer sacar? R$'))
    if len(a) == 1:
        print('Total de {} cédulas de R$1,00'.format(a))
        break
    
    if len(a) == 2:
        b = int(a[0])*10         
        resto10 = b // 10
        #notas de 10
        if d >= 10:
            resto1 = d // 10
            n10 = resto1
            #notas de 1
            n1 = d - 10
            print('Total:\n{} notas de R$50,00 \n{} notas de R$20,00 \n{} notas de R$10,00 \n{} notas de R$1,00'.format(n50, n20, n10, n1))
            break
