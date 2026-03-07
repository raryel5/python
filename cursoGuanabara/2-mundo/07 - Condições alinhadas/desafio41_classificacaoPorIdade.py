from datetime import date
anoat = date.today().year
nome = input('Qual o nome do atleta?\n')
nasc = int(input('Qual o ano de nascimento? '))
idade = anoat - nasc

if idade <= 9:
    print('O atleta \033[1m {}\033[m tem {} anos e está na categoria \033[1;30mMIRIM\033[m.'.format(nome, idade))
elif idade <= 14:
    print('O atleta \033[1m {}\033[m tem {} anos e está na categoria \033[1;31mINFANTIL\033[m.'.format(nome, idade))
elif idade <= 19:
    print('O atleta \033[1m {}\033[m tem {} anos e está na categoria \033[1;32mJUNIOR\033[m.'.format(nome, idade))
elif idade <= 20:
    print('O atleta \033[1m {}\033[m tem {} anos e está na categoria \033[1;33mSENIOR\033[m.'.format(nome, idade))
elif idade > 20:
    print('O atleta \033[1m {}\033[m tem {} anos e está na categoria \033[1;34mMASTER\033[m.'.format(nome, idade))
