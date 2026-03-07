precos = {'cebola':2, 'alho': 3, 'banana':4}
precosDuplicados = {}

for chave, valor in precos.items():
    precosDuplicados[chave] = valor * 2

print(precosDuplicados)

# Salva chave:valor em cada linha
with open('dados.txt', 'w', encoding='utf-8') as arquivo:
    for chave, valor in precosDuplicados.items():
        arquivo.write(f'{chave}: {valor}x\n')