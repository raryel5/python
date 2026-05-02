from tkinter.filedialog import askdirectory, askopenfilename, askopenfilenames

# pasta = askdirectory(title="Selecione a pasta desejada")
# print(pasta)

# selecionar um arquivo
# arquivo = askopenfilename(title="Selecione o arquivo")
# print(arquivo)

# selecionar vários arquivos e retorna uma tupla
arquivo = askopenfilenames(title="Selecione o arquivo")
print(arquivo)




#
# Referências:
# https://youtu.be/3AdoZoCvrv4?si=DdhJakNX7IekhszH