import random
a = int(1)
while a != 0:
    x = random.randint(0,4)
    if x == 0:
        comp = 'PEDRA'
    elif x == 1:
        comp = 'PAPEL'
    elif x == 2:
        comp = 'TESOURA'
    elif x == 3:
        comp = 'LAGARTO'
    elif x == 4:
        comp = 'SPOCK'
    
    print('\033[1;33;40m====  Jokenpo TBBT  ====')
    print('== ESCOLHA UMA OPÇÃO ==\033[1;32m')
    print('[0] PEDRA')
    print('[1] PAPEL')
    print('[2] TESOURA')
    print('[3] LAGARTO')
    print('[4] SPOCK\033[m')
    suaMao = int(input('Sua opção: '))
    if suaMao == 0:
        vc = 'PEDRA'
    elif suaMao == 1:
        vc = 'PAPEL'
    elif suaMao == 2:
        vc = 'TESOURA'
    elif suaMao == 3:
        vc = 'LAGARTO'
    elif suaMao == 4:
        vc = 'SPOCK'
        
    print('Você escolheu {}! e o computador escolheu {}.'.format(vc, comp))

    #1
    if x == suaMao:
        print('\033[1;36mEMPATE!\033[m')
        op = input('Quer jogar de novo? s/n.')
        if op == 'n':
            a = 0
            print('\033[1;31;mFIM DE JOGO\033[m')
    #2
    elif x == 0 and suaMao == 1:
        print('Papel enrola Pedra!')
        print('\033[1;34mVOCÊ GANHOU!\033[m')
        op = input('Quer jogar de novo? s/n.')
        if op == 'n':
            a = 0
            print('\033[1;31;mFIM DE JOGO\033[m')
    #3
    elif x == 0 and suaMao == 2:
        print('Pedra quebra Tesoura!')
        print('\033[1;31mGAME OVER\033[m')
        op = input('Quer jogar de novo? s/n.')
        if op == 'n':
            a = 0
            print('\033[1;31;mFIM DE JOGO\033[m')
    #4
    elif x == 0 and suaMao == 3:
        print('Pedra mata Lagarto!')
        print('\033[1;31mGAME OVER!\033[m')
        op = input('Quer jogar de novo? s/n.')
        if op == 'n':
            a = 0
            print('\033[1;31;mFIM DE JOGO\033[m')
    #5
    elif x == 0 and suaMao == 4:
        print('Spock quebra Pedra!')
        print('\033[1;34mVOCÊ GANHOU!\033[m')
        op = input('Quer jogar de novo? s/n.')
        if op == 'n':
            a = 0
            print('\033[1;31;mFIM DE JOGO\033[m')
    #6
    elif x == 1 and suaMao == 0:
        print('Papel enrola Pedra!')
        print('\033[1;31mGAME OVER!\033[m')
        op = input('Quer jogar de novo? s/n.')
        if op == 'n':
            a = 0
            print('\033[1;31;mFIM DE JOGO\033[m')
    #7
    elif x == 1 and suaMao == 2:
        print('Tesoura corta Papel!')
        print('\033[1;34mVOCÊ GANHOU!\033[m')
        op = input('Quer jogar de novo? s/n.')
        if op == 'n':
            a = 0
            print('\033[1;31;mFIM DE JOGO\033[m')
    #8
    elif x == 1 and suaMao == 3:
        print('Lagarto come Papel!')
        print('\033[1;34mVOCÊ GANHOU!\033[m')
        op = input('Quer jogar de novo? s/n.')
        if op == 'n':
            a = 0
            print('\033[1;31;mFIM DE JOGO\033[m')
    #9
    elif x == 1 and suaMao == 4:
        print('spock rasga Papel!')
        print('\033[1;34mVOCÊ GANHOU!\033[m')
        op = input('Quer jogar de novo? s/n.')
        if op == 'n':
            a = 0
            print('\033[1;31;mFIM DE JOGO\033[m')
    #10
    elif x == 2 and suaMao == 0:
        print('Pedra quebra Tesoura!')
        print('\033[1;34mVOCÊ GANHOU!\033[m')
        op = input('Quer jogar de novo? s/n.')
        if op == 'n':
            a = 0
            print('\033[1;31;mFIM DE JOGO\033[m')
    #11
    elif x == 2 and suaMao == 1:
        print('Tesoura corta Papel!')
        print('\033[1;31mGAME OVER!\033[m')
        op = input('Quer jogar de novo? s/n.')
        if op == 'n':
            a = 0
            print('\033[1;31;mFIM DE JOGO\033[m')
    #12
    elif x == 2 and suaMao == 3:
        print('Tesoura mata Lagarto!')
        print('\033[1;31mGAME OVER!\033[m')
        op = input('Quer jogar de novo? s/n.')
        if op == 'n':
            a = 0
            print('\033[1;31;mFIM DE JOGO\033[m')
    #13
    elif x == 2 and suaMao == 4:
        print('Spock quebra Tesoura!')
        print('\033[1;34mVOCÊ GANHOU!\033[m')
        op = input('Quer jogar de novo? s/n.')
        if op == 'n':
            a = 0
            print('\033[1;31;mFIM DE JOGO\033[m')
    #14
    elif x == 3 and suaMao == 0:
        print('Pedra mata Lagarto!')
        print('\033[1;34mVOCÊ GANHOU!\033[m')
        op = input('Quer jogar de novo? s/n.')
        if op == 'n':
            a = 0
            print('\033[1;31;mFIM DE JOGO\033[m')
    #15
    elif x == 3 and suaMao == 1:
        print('Lagarto come Papel!')
        print('\033[1;31mGAME OVER!\033[m')
        op = input('Quer jogar de novo? s/n.')
        if op == 'n':
            a = 0
            print('\033[1;31;mFIM DE JOGO\033[m')
    #16
    elif x == 3 and suaMao == 2:
        print('Tesoura mata Lagarto!')
        print('\033[1;34mVOCÊ GANHOU!\033[m')
        op = input('Quer jogar de novo? s/n.')
        if op == 'n':
            a = 0
            print('\033[1;31;mFIM DE JOGO\033[m')
    #17
    elif x == 3 and suaMao == 4:
        print('Lagarto envenena Spock!')
        print('\033[1;31mGAME OVER!\033[m')
        op = input('Quer jogar de novo? s/n.')
        if op == 'n':
            a = 0
            print('\033[1;31;mFIM DE JOGO\033[m')
    #18
    elif x == 4 and suaMao == 0:
        print('Spock quebra Pedra!')
        print('\033[1;31mGAME OVER!\033[m')
        op = input('Quer jogar de novo? s/n.')
        if op == 'n':
            a = 0
            print('\033[1;31;mFIM DE JOGO\033[m')
    #19
    elif x == 4 and suaMao == 1:
        print('spock rasga Papel!')
        print('\033[1;31mGAME OVER!\033[m')
        op = input('Quer jogar de novo? s/n.')
        if op == 'n':
            a = 0
            print('\033[1;31;mFIM DE JOGO\033[m')
    #20
    elif x == 4 and suaMao == 2:
        print('Spock quebra Tesoura!')
        print('\033[1;31mGAME OVER!\033[m')
        op = input('Quer jogar de novo? s/n.')
        if op == 'n':
            a = 0
            print('\033[1;31;mFIM DE JOGO\033[m')
    #21
    elif x == 4 and suaMao == 3:
        print('Lagarto envenena Spock!')
        print('\033[1;34mVOCÊ GANHOU!\033[m')
        op = input('Quer jogar de novo? s/n.')
        if op == 'n':
            a = 0
            print('\033[1;31;mFIM DE JOGO\033[m')
