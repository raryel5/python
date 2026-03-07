from datetime import date
anoatual = date.today().year
nascimento = int(input('E qual ano você nasceu? '))
idade = anoatual - nascimento
if idade == 18:
    print('Você tem {} anos, procure a junta militar mais próxima e aliste-se.'.format(idade))
elif idade < 18:
    tempo = 18 - idade
    print('Ainda faltam {} anos para você completar 18 anos.'.format(tempo))
    anoalis = anoatual + tempo
    print('Você deverá se alistar no ano de {}'.format(anoalis))
elif idade > 18:
    tempo = idade - 18
    print('Se passaram {} anos do seu tempo correto de alistamento.'.format(tempo))
    anoalis = anoatual - tempo
    print('Você deveria ter se alistado em {}.'.format(anoalis))
