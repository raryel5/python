l=int(input('Qual a largura (metros) da parede? '))
a=int(input('Qual a altura (metros) da parede? '))
print('Sua parede tem dimensão de {}x{}m² e sua área é de {}m².'.format(l, a, l*a, ))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format((l*a)/2))
