m = float(input('Qual a sua massa (kg): '))
h =  float(input('Qual a sua altura (metros): '))
imc = m/(h**2)

if imc < 18.5:
    print('\033[4;33;47m Você está abaixo do peso.')
    
elif imc > 18.5 and imc < 25:
    print('\033[4;32;47m Você está no peso ideal.')
    
elif imc > 25 and imc < 30:
    print('\033[4;33;47m Você está com sobrepeso.')

elif imc > 30 and imc < 40:
    print('\033[4;33;47m Você está obeso.')

elif imc > 40:
    print('\033[4;31;47m Você está com obsidade mórbida.')

print('\033[m')
