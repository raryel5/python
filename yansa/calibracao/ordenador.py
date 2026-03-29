import csv

class Ordenador:
    """
    Classe para ordenar listas usando algoritimo quicksort.

    """
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.campo = []
        self.campoColum = []

    def extractColunm(self):
        with open(self.arquivo, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for linha in reader:
                self.campo.append(float(linha['Valor']))

            # passo para converter a coluna de strings em coluna de floats
            # for i in range(len(self.campoColum) - 1):
            #     self.campo.append(float(self.campoColum[i]))

        print(f"Coluna foi importada com sucesso.")

        print(f"Iniciando ordenação da coluna...")
        # return self.quicksort(self.campo)
        # return self.campo.sort()
        listaOrdenada = self.campo
        listaOrdenada.sort()

        for i in range(10):
            print(listaOrdenada[i])

        
    def quicksort(self, array):
        if len(array) < 2:
            return array
        
        pivo = array[0]
        menores = []
        maiores = []
        for i in array[1:]:
            if i <= pivo:
                menores.append(i)
            else:
                maiores.append(i)

        return self.quicksort(menores) + [pivo] + self.quicksort(maiores)

# array = [15, 10, 33, 5, 6, 1, 4, 33, 13, 54, 42, 2]
# array = [15, 10, 33, 5]
objetoLista = Ordenador("listaNormalizada.csv")
objetoLista.extractColunm()

# print(objetoLista.quicksort(array))
