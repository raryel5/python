import csv
import matplotlib.pyplot as plt

campo = []
arquivo = "freg_2026-03-08.csv"
# arquivo = "RASP0004-17h-UTC.csv"
# arquivo = "fm0220.csv"

indice = 2

with open(arquivo, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    # reader = csv.DictReader(file)
    next(reader)
    for linha in reader:
        # campo.append(float(linha['Electric_Field_V_m']))
        # campo.append(float(linha['fm0220']))
        campo.append(linha[indice])


# print(len(campo))
campoFloat = []
k = len(campo)
for i in range(len(campo) - 1):
    campoFloat.append(float(campo[i]))

print(type(campo[0]))
print(campo[0])

print(type(campoFloat[0]))
print(campoFloat[0])
