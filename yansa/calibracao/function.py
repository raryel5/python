import csv
import matplotlib.pyplot as plt

class FunctionsCalc:
    """
    Classe para fazer cálculos de calibração em sensores de campo elétrico.

    Para usar a função plotContra insira primeiro a coluna a ser calibrada, em seguida a coluna de referência.
    plotContra("X","Y")

    A função normalizar utiliza hashmap para otmizar os cálculos.

    """
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.campo = []
        self.campoColum = []
        self.variacao = []
        self.tempo = []
        self.p = 0
        self.pi = 0
        self.Eatual = 0
        self.Eantes = 0
        self.colunmNorm = []
        self.colunmOrden = []


    def extractColumn(self, coluna):
        self.campo = []
        with open(self.arquivo, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for linha in reader:
                self.campo.append(float(linha[coluna]))

            # passo para converter a coluna de strings em coluna de floats
            for i in range(len(self.campoColum) - 1):
                self.campo.append(float(self.campoColum[i]))

    def calcVariacao(self, m = 0):
        k = len(self.campo)

        if m >= k:
            return self.variacao, self.p, self.pi, self.Eatual, self.Eantes

        for i in range(m, k):
            if i == 0:
                self.variacao.append(0)
                self.tempo.append(0)
                count = 7

            else:        
                self.Eatual = self.campo[i]
                self.Eantes = self.campo[i-1]

            var = self.Eatual - self.Eantes
            self.variacao.append(var)
            self.tempo.append(i)
            m += 1

            dE = abs(var)
            if dE >= 50 and dE < 100 and count > 5:
                self.p += 1
                count = 0

            elif dE >= 100 and count > 5:
                self.pi += 1
                count = 0

            count += 1

        return self.calcVariacao(m)

    def normalizar(self, coluna):
        self.extractColumn(coluna)
        # print(f"O valor máximo de {coluna} é {max(self.campo)}")
        # print(f"O valor mínimo de {coluna} é {min(self.campo)}")

        # hashmap/dicionário
        hashLista = {}
        listaNormal = []

        for i in range(len(self.campo)-1):
            if hashLista.get(self.campo[i]):
                listaNormal.append(hashLista[self.campo[i]])

            else:
                valueNorm = (self.campo[i] - min(self.campo))/(max(self.campo)-min(self.campo))
                hashLista[self.campo[i]] = valueNorm # arredondado para 4 casas decimais
                listaNormal.append(valueNorm)
        
        # self.exportCSV(listaNormal, f'{coluna}-norm.csv')

        # return self.quicksort(listaNormal)
        self.colunmOrden = listaNormal
        self.colunmOrden.sort()
        # self.exportCSV(self.colunmOrden, 'listaOrdenada.csv')

    # Método de Ordenação Quicksort
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

    def exportCSV(self, lista, name):
        # Abrir arquivo para escrita ('w'), usando 'newline' para evitar linhas em branco extras
        with open(name, 'w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)

            # Escrever cabeçalho (opcional)
            writer.writerow(['Valor'])

            # Escrever todas as linhas de uma vez
            # writer.writerows(lista)

            # Escreve os dados (cada número em uma linha)
            for value in lista:
                writer.writerow([value])

        print("CSV exportado com sucesso!")

    def plotar(self, coluna):
        self.extractColumn(coluna)

        self.calcVariacao()

        print("Quantidade de pulsos: ", self.p)
        print("Quantidade de pulsos intensos: ", self.pi)

        # configurações de plotagem
        ## padrão de estilo
        plt.style.use('ggplot')
        plt.figure(figsize=(8,5))

        plt.title('Variações de campo e pulsos - Python', fontsize=16, fontweight='bold', fontfamily='monospace')
        plt.xlabel('tempo', fontsize=10, fontfamily='monospace')
        plt.ylabel('V/m', fontsize=10, fontfamily='monospace')

        legenda = "Pulsos: " + str(self.p) + "\n PI: " + str(self.pi)

        plt.scatter(self.tempo, self.variacao, label=legenda)
        plt.legend(fontsize=12, frameon=True, framealpha=0.7 , facecolor='white')
        
        return plt.show()

    def plotContra(self, colunaX, colunaY):
        self.normalizar(colunaX)
        Xcolunm = self.colunmOrden
        print(f"o tamanho de X é {len(Xcolunm)}")

        self.normalizar(colunaY)
        Ycolunm = self.colunmOrden
        print(f"o tamanho de Y é {len(Ycolunm)}")

        # configurações de plotagem
        ## padrão de estilo
        plt.style.use('ggplot')
        plt.figure(figsize=(8,5))
        #
        plt.title('Curva de Calibração', fontsize=16, fontweight='bold', fontfamily='monospace')
        plt.xlabel('Sensor para calibrar: ' + colunaX, fontsize=10, fontfamily='monospace')
        plt.ylabel('Referência: ' + colunaY, fontsize=10, fontfamily='monospace')
        #
        plt.scatter(Xcolunm, Ycolunm)
        plt.legend(fontsize=12, frameon=True, framealpha=0.7 , facecolor='white')
        
        return plt.show()

