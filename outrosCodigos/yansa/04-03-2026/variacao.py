import csv
import matplotlib.pyplot as plt

campo = []
arquivo = "spsul-12h-a-13h-UTC.csv"
# arquivo = "RASP0004-17h-UTC.csv"
# arquivo = "fm0229.csv"

with open(arquivo, mode='r') as file:
    reader = csv.DictReader(file)
    for linha in reader:
        # campo.append(float(linha['Electric_Field_V_m']))
        campo.append(float(linha['fm0209']))

# print(len(campo))

variacao = []
tempo = []
p = 0
pi = 0
Eatual = 0
Eantes = 0

def calcVariacao(k, m = 0):
    global variacao, campo, tempo,  p, pi, Eatual, Eantes

    if m >= k:
        return variacao, p, pi, Eatual, Eantes

    for i in range(m, k):
        if i == 0:
            variacao.append(0)
            tempo.append(0)
            count = 7

        else:        
            Eatual = campo[i]
            Eantes = campo[i-1]

        var = Eatual - Eantes
        variacao.append(var)
        tempo.append(i)
        m += 1

        dE = abs(var)
        if dE >= 50 and dE < 100 and count > 6:
            p += 1
            count = 0

        elif dE >= 100 and count > 6:
            pi += 1
            count = 0

        count += 1

    return calcVariacao(k, m)

k = len(campo)
calcVariacao(k)
print("Campo:", campo[830])
print("O valor da posição 831 é: ", variacao[831])
# print("Campo anterior: ", eAntes)
# print("Campo atual: ", eAtual)

# print("campo real anterior: ", campo[157])
# print("campo real atual: ", campo[158])


# x = list(range(len(variacao)))
print("Quantidade de pulsos: ", p)
print("Quantidade de pulsos intensos: ", pi)

# 
# configurações de plotagem
#
# padrão de estilo
plt.style.use('ggplot')
plt.figure(figsize=(8,5))

# plt.ion()

# plt.title('variações de campo e pulsos', fontsize=16, fontweight='bold', fontstyle='italic', fontfamily='monospace')
plt.title('Variações de campo e pulsos - Python', fontsize=16, fontweight='bold', fontfamily='monospace')
plt.xlabel('tempo', fontsize=10, fontfamily='monospace')
plt.ylabel('V/m', fontsize=10, fontfamily='monospace')
# plt.tight_layout()

legenda = "Pulsos: " + str(p) + "\n PI: " + str(pi)

# plt.scatter(x, variacao, label="pulsos")
plt.scatter(tempo, variacao, label=legenda)
plt.legend(fontsize=12, frameon=True, framealpha=0.7 , facecolor='white')
plt.show()

# plt.pause(5)

# plt.ioff()

# Plot número 2
# plt.scatter(tempo, campo, label=legenda)
# plt.legend(fontsize=12, frameon=True, framealpha=0.7 , facecolor='white')
# plt.show()


# Data ISO 8601 (com fuso UTC 'Z')
# iso_date = "2023-10-27T10:00:00Z"

# Converte para objeto datetime
# dt = datetime.fromisoformat(iso_date.replace('Z''+00:00'))

# Converte para timestamp (segundos)
# timestamp = dt.timestamp()

# from datetime import datetime
# dt = datetime.strptime("2026-02-26T00:00:00""%Y-%m-%dT%H:%M:%S")
# timestamp = int(dt.timestamp())