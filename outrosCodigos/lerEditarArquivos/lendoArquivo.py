documento = 'email2.txt'
# temLinhaBranco = False

nLinhasBrancas = 0
with open(documento, 'r') as arquivo:
    for i, linha in enumerate(arquivo, 1):
        if not linha.strip():  # strip() remove \n, \t e espaços
            # temLinhaBranco = True
            print(f"linha em branco na linha {i}")
            nLinhasBrancas += 1
    if nLinhasBrancas == 0:
        print(f"Sem linhas em branco!")

            # break  # Encontrou uma, não precisa continuar

# if temLinhaBranco:
#     print("O arquivo contém linhas em branco.")
# else:
#     print("O arquivo não contém linhas em branco.")
