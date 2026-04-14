import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.optimize import minimize
from sklearn.metrics import r2_score


class FunctionsCalc:
    """
    # Classe FunctionsCalc
    Autor: Renan Aryel

    Classe para fazer cálculos de calibração em sensores de campo elétrico utilizando dados de campo elétrico salvos no formato CSV. O objetivo é obter os coeficientes de um polinômio de grau 3 para ajustar os dados de um sensor em função de outro de referência.

    Para criar o objeto desta classe insira o nome do arquivo CSV como:
    Ex: sensor.FunctionsCalc("nomeDoArquivo.csv")

    Depois é só aplicar os métodos desejados para trabalhar com esses dados.

    # Método extractColunm()

    Passe o nome da coluna para que o método retorne os valores dessa coluna do CSV como uma instância. Os demais métodos utilizam esse como base para os cálculos.

    # Método normalizar()

    O método normalizar() executa uma normalização de 0 a 1 para um coluna especificada e ordena essa coluna por meio do método sort() do Python. Esse método utiliza hashmap para otmizar os cálculos de normalização.
    Ex: nomeDoObjeto.normalizar("nomeDaColunaNoCSV")

    # Método plotContra()

    Para usar a função plotContra insira primeiro a coluna a ser calibrada, em seguida a coluna de referência.
    plotContra("X","Y")

    # Método ajustePolinomial()

    Esse método pega os dados normalizados e busca os coeficientes de um polinômio de ordem 3 que se ajusta aos dados. No final ele plota a curva do método plotContra() e mostra os coeficientes.

    # Referências
    - Ajuste Polinomial: https://www.monolitonimbus.com.br/ajuste-de-funcoes-no-python/


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

        # return f"O valor máximo de {coluna} normalizada é {max(self.colunmOrden)}.\nO valor mínimo de {coluna} normalizada é {min(self.colunmOrden)}"

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

    def correlacaoBruta(self, colunaX, colunaY):

        self.extractColumn(colunaX)
        Xcolunm = self.campo

        self.extractColumn(colunaY)
        Ycolunm = self.campo

        data = {
            'variavel_x': Xcolunm,
            'variavel_y': Ycolunm
        }
        df = pd.DataFrame(data)

        # Calcular correlação de Pearson (padrão)
        correlacao = df['variavel_x'].corr(df['variavel_y'])
        print(f"Correlação: {correlacao}")
    
    def correlacaoNormalized(self, colunaX, colunaY):

        print("Iniciando normalização e ordenação dos dados...")

        self.normalizar(colunaX)
        Xcolunm = self.colunmOrden

        self.normalizar(colunaY)
        Ycolunm = self.colunmOrden

        print("Normalização completa.")

        data = {
            'variavel_x': Xcolunm,
            'variavel_y': Ycolunm
        }
        df = pd.DataFrame(data)

        ## Calcular correlação de Pearson (padrão)
        print("Calculando correlação de Pearson...")
        correlacao = df['variavel_x'].corr(df['variavel_y'])
        print(f"Correlação: {correlacao}")
        print(len(self.campo))

    def ajustePolinBruto(self, colunaX, colunaY):
        
        self.extractColumn(colunaX)
        Xcolunm = self.campo

        self.extractColumn(colunaY)
        Ycolunm = self.campo

        x = np.array(Xcolunm)
        y = np.array(Ycolunm)

        #
        ## com Sklearn
        #
        r2 = r2_score(x, y)
        print(f"O R-quadrado: {r2:.3f}")

        print("Iniciando ajuste polinomial...")

        def func(x, a, b, c, d):
            return a*x**3 + b*x**2 + c*x + d

        popt, pcov = curve_fit(func, x, y)

        print("Ajuste completo!")

        fig, ax = plt.subplots()

        legenda = f'%5.6f x³ + %5.6f x² + %5.6f x + %5.6f\n{r2:.4f}' %tuple(popt) 
        
        plt.grid(True)
        plt.plot(x, y, '*')
        plt.plot(x, func(x, *popt), label=legenda)
        plt.legend(fontsize=12, frameon=True, framealpha=0.7, facecolor='white')     

        plt.title('Ajuste polinomial de grau 3')
        plt.show()

    def ajustePolinomial(self, colunaX, colunaY):
        print("Iniciando normalização e ordenação dos dados...")

        self.normalizar(colunaX)
        Xcolunm = self.colunmOrden

        self.normalizar(colunaY)
        Ycolunm = self.colunmOrden

        print("Normalização completa.")
        print("Calculando o R-quadrado...")

        x = np.array(Xcolunm)
        y = np.array(Ycolunm)

        # ## Soma dos Quadrados dos Resíduos (SSR)
        # ss_res = np.sum((x - y) ** 2)
        # print(f"SSR: {ss_res}")
        
        # ## Soma Total dos Quadrados (TSS)
        # media = np.mean(y)
        # ss_tot = np.sum((y - media) ** 2)
        # print(f"TSS: {ss_tot}")

        # ## R-quadrado
        # r2 = 1 - (ss_res / ss_tot)
        # print(f"R-quadrado: {r2:.3f}")

        #
        ## com Sklearn
        #
        r2 = r2_score(x, y)
        print(f"O R-quadrado: {r2:.3f}")


        print("Iniciando ajuste polinomial...")

        def func(x, a, b, c, d):
            return a*x**3 + b*x**2 + c*x + d

        popt, pcov = curve_fit(func, x, y)

        print("Ajuste completo!")

        fig, ax = plt.subplots()

        legenda = f'%5.6f x³ + %5.6f x² + %5.6f x + %5.6f\n{r2:.4f}' %tuple(popt)
        # legenda = "f(x) = ax³ + bx² + cx + d"
        # legenda = f'a=%5.6f\nb=%5.6f\nc=%5.6f\nd=%5.6f' %tuple(popt)        
        
        plt.grid(True)
        plt.plot(x, y, '*')
        plt.plot(x, func(x, *popt), label=legenda)
        plt.legend(fontsize=12, frameon=True, framealpha=0.7, facecolor='white')
        # textstr = 'a=%5.4f\nb=%5.4f\nc=%5.4f\nd=%5.4f' %tuple(popt)

        # ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=10, verticalalignment='top')        

        plt.title('Ajuste polinomial de grau 3')
        plt.show()

        # deg = 3
        # z = np.polyfit(x, y, deg)
        # y2 = np.poly1d(z)

        # plt.plot(x, y, "*")
        # plt.plot(x, y2(x), "-")
        # plt.title('Ajuste polinomial de grau 3')
        # plt.show()

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

