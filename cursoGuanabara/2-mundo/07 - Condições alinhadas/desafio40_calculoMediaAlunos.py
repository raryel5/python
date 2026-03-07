nome = input("Qual o nome do aluno(a)? ")
n1 = float(input("\033[m Digite a primeira nota do aluno n1 = "))
n2 = float(input("Digite a primeira nota do aluno n2 = "))

med = (n1+n2)/2

if med < 5:
    print('O aluno(a) \033[1m {}\033[m está \033[1;31m REPROVADO\033[m'.format(nome))

elif med >= 5 and med <= 6.9:
    print('O aluno(a) \033[1m {}\033[m está de \033[1;33m RECUPERAÇÃO\033[m'.format(nome))

elif med > 6.9:
    print('O aluno(a)\033[1m {}\033[m está \033[1;34m APROVADO.\033[m'.format(nome))
