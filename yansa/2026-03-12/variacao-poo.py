import csv
import matplotlib.pyplot as plt

class Pulsodetect:
    """
    Classe para detectar pulsos elétricos.
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

    def plotar(self, coluna):
        self.extractColumn(coluna)

        self.calcVariacao()

        print("Quantidade de pulsos: ", self.p)
        print("Quantidade de pulsos intensos: ", self.pi)

        # 
        # configurações de plotagem
        #
        # padrão de estilo
        plt.style.use('ggplot')
        plt.figure(figsize=(8,5))

        plt.title('Variações de campo e pulsos - Python', fontsize=16, fontweight='bold', fontfamily='monospace')
        plt.xlabel('tempo', fontsize=10, fontfamily='monospace')
        plt.ylabel('V/m', fontsize=10, fontfamily='monospace')

        legenda = "Pulsos: " + str(self.p) + "\n PI: " + str(self.pi)

        plt.scatter(self.tempo, self.variacao, label=legenda)
        plt.legend(fontsize=12, frameon=True, framealpha=0.7 , facecolor='white')
        
        return plt.show()

fm0234 = Pulsodetect("fm0234.csv")

fm0234.plotar("Electric_Field_V_m")