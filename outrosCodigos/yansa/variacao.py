import csv
import matplotlib.pyplot as plt

campo = []

with open('fm0229.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for linha in reader:
        campo.append(float(linha['Electric_Field_V_m']))

# print(len(campo))

variacao = []
tempo = []
p = 0
pi = 0
eAtual = 0
eAntes = 0

def calcVariacao(k, m = 0):
    global variacao, p, pi, campo, tempo, eAtual, eAntes

    if m >= k:
        return variacao, p, pi, eAtual, eAntes

    for i in range(m, k):
        if i == 0:
            variacao.append(0)
            tempo.append(0)
        else:        
            eAtual = campo[i]
            eAntes = campo[i-1]

        var = eAtual - eAntes
        variacao.append(var)
        tempo.append(i)
        m += 1

        if var >= 50 and var < 100:
            p += 1
            # m += 6

        if var >= 100:
            pi += 1
            # m += 6

    return calcVariacao(k, m)

k = len(campo)
calcVariacao(k)
# print(campo[k])
# print("O valor da posição 692 é: ", variacao[159])
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


# Data ISO 8601 (com fuso UTC 'Z')
# iso_date = "2023-10-27T10:00:00Z"

# Converte para objeto datetime
# dt = datetime.fromisoformat(iso_date.replace('Z''+00:00'))

# Converte para timestamp (segundos)
# timestamp = dt.timestamp()

# from datetime import datetime
# dt = datetime.strptime("2026-02-26T00:00:00""%Y-%m-%dT%H:%M:%S")
# timestamp = int(dt.timestamp())