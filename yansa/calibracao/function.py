import csv
import matplotlib.pyplot as plt

class FunctionsCalc:
    """
    Classe para detectar pulsos elétricos.

    Para usar a função plotContra insira primeiro a coluna a ser calibrada, em seguida a coluna de referência.
    plotContra("X","Y")
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

        for i in range(len(self.campo)-1):
            valueNorm = (self.campo[i] - min(self.campo))/(max(self.campo)-min(self.campo))
            self.colunmNorm.append(valueNorm)

        self.colunmOrdem = self.quicksort(self.colunmNorm)
        
        # array.sort()

        # Ordenação Bluble sort
        # for j in range(len(array)-1):
        #     for i in range(len(array)-1-j):
        #         if array[i] > array[i+1]:
        #             a = array[i+1]
        #             array[i+1] = array[i]
        #             array[i] = a

    # Ordenação Quicksort
    def quicksort(self, array):
        if len(array) < 2:
            return array
        else:
            pivo = array[0]
            menores = [i for i in array[1:] if i <= pivo]
            maiores = [i for i in array[1:] if i > pivo]                
            return self.quicksort(menores) + [pivo] + self.quicksort(maiores)

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
        Xcolunm = self.colunmOrdem

        self.normalizar(colunaY)
        Ycolunm = self.colunmOrdem

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

