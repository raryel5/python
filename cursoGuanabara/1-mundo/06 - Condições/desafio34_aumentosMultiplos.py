# Escreva um programa que pergunte o salário de um funcionário e calcule
# o valor do seu aumento. Para salários superiores a 1250 calcule aumento de 10%,
# para inferiores ou iguais o aumento é de 15%
salario = float(input('Qual o salário atual do funcionário? '))
if salario <= 1250:
    nsalario = salario + (salario * 15/100)
    per = 15
else:
    nsalario = salario + (salario * 10/100)
    per = 10

print('O aumento foi de {}% e o novo salário é R${:.2f}.'.format(per, nsalario))
