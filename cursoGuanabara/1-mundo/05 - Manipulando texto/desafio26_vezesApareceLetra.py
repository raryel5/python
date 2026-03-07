nome = str(input('Digite uma frase: '))
print('A letra \'A\' aparece {} vezes'.format(nome.lower().count('a')))
print('A letra \'A\' aparece pela primeira vez em {}'.format(nome.lower().find('a')))
print('A letra \'A\' aparece pela última vez na posição {}.'.format(nome.lower().rfind('a')))
