import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import seaborn as sns
import plotly.express as px
from scipy.optimize import curve_fit
from scipy.optimize import minimize
from sklearn.metrics import r2_score


class FunctionsCalc:
    """
    # Classe FunctionsCalc
    Autor: Renan Aryel

    Classe para fazer cálculos de calibração em sensores de campo elétrico
    utilizando dados de campo elétrico salvos no formato CSV.
    O objetivo é obter os coeficientes de um polinômio de grau 3 para
    ajustar os dados de um sensor em função de outro de referência.

    Para criar o objeto desta classe insira o nome do arquivo CSV como:
    Ex: sensor.FunctionsCalc("nomeDoArquivo.csv")

    Depois, é só aplicar os métodos desejados para trabalhar com esses dados.

    --- MÉTODOS ---
    # Método extractColunm()
    Passe o nome da coluna para que o método retorne os valores dessa coluna do CSV como uma instância. Os demais métodos utilizam esse como base para os cálculos.

    # Método normalizar()
    O método normalizar() executa uma normalização de 0 a 1 para um coluna especificada e ordena essa coluna por meio do método sort() do Python. Esse método utiliza hashmap para otmizar os cálculos de normalização.
    Ex: nomeDoObjeto.normalizar("tituloDaColunaNoCSV")

    # Método exportCSV()
    Exporta uma lista em formato csv. Esse método é utilizado dentro de outros métodos.
    Sintaxe: exportCSV(lista, nomeDoArquivo)
    Ex: exportCSV(Xcolunm, "colunax.csv")

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
        self.dadosTratados = []
        self.media = 0
        self.dp = 0
        self.delta = 0


    def extractColumn(self, coluna):
        self.campo = []
        with open(self.arquivo, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for linha in reader:
                self.campo.append(float(linha[coluna]))

            # passo para converter a coluna de strings em coluna de floats
            for i in range(len(self.campoColum) - 1):
                self.campo.append(float(self.campoColum[i]))

            self.media = np.mean(self.campo)

            # Definir um intervalo específico
            # listaTemp = self.campo[166050:254700]
            listaTemp = self.campo[30000:100000]
            # listaTemp = self.campo[120000:170000]
            self.campo = listaTemp
            # print(f"Tamanho do intervalo gerado: {len(self.campo)}")


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
        lista = []

        for i in range(len(self.campo)):
            if hashLista.get(self.campo[i]):
                lista.append(hashLista[self.campo[i]])

            else:
                # normalização entre -1 e 1
                valueNorm = (2*(self.campo[i] - min(self.campo))/(max(self.campo)-min(self.campo)))-1
                hashLista[self.campo[i]] = valueNorm # arredondado para 4 casas decimais
                lista.append(valueNorm)

                # normalização entre 0 e 1
                # valueNorm = (self.campo[i] - min(self.campo))/(max(self.campo)-min(self.campo))
                # hashLista[self.campo[i]] = valueNorm # arredondado para 4 casas decimais
                # lista.append(valueNorm)
        
        # self.exportCSV(listaNormal, f'{coluna}-norm.csv')

        # return self.quicksort(listaNormal)
        self.colunmNorm = lista
        self.colunmOrden = lista
        self.colunmOrden.sort()

        # self.exportCSV(self.colunmOrden, 'listaOrdenada.csv')

        # return f"O valor máximo de {coluna} normalizada é {max(self.colunmOrden)}.\nO valor mínimo de {coluna} normalizada é {min(self.colunmOrden)}"
    
    def normalizar2(self, dados):
        
        # hashmap/dicionário
        hashLista = {}
        lista = []

        for i in range(len(dados)):
            if hashLista.get(dados[i]):
                lista.append(hashLista[dados[i]])

            else:
                # normalização entre -1 e 1
                valueNorm = (2*(dados[i] - min(dados))/(max(dados)-min(dados)))-1
                hashLista[dados[i]] = valueNorm # arredondado para 4 casas decimais
                lista.append(valueNorm)

                # normalização entre 0 e 1
                # valueNorm = (dados[i] - min(dados))/(max(dados)-min(dados))
                # hashLista[dados[i]] = valueNorm # arredondado para 4 casas decimais
                # lista.append(valueNorm)
        
        # self.exportCSV(listaNormal, f'{coluna}-norm.csv')
        self.colunmNorm = lista
        self.colunmOrden = lista
        self.colunmOrden.sort()

    def padronizar(self, coluna):
        self.extractColumn(coluna)
        # print(f"O valor máximo de {coluna} é {max(self.campo)}")
        # print(f"O valor mínimo de {coluna} é {min(self.campo)}")

        # hashmap/dicionário
        hashLista = {}
        lista = []

        media = np.mean(self.campo)
        desv_padrao = np.std(self.campo)

        for i in range(len(self.campo)-1):
            if hashLista.get(self.campo[i]):
                lista.append(hashLista[self.campo[i]])

            else:
                # Formula de padronização:
                valuePadron = (self.campo[i] - media)/(desv_padrao)

                hashLista[self.campo[i]] = valuePadron # arredondado para 4 casas decimais
                lista.append(valuePadron)
        
        self.colunmPadron = lista
        self.colunmOrden = lista
        self.colunmOrden.sort()

        # self.exportCSV(self.colunmOrden, 'listaOrdenada.csv')
        # return f"O valor máximo de {coluna} padronizada é {max(self.colunmOrden)}.\nO valor mínimo de {coluna} normalizada é {min(self.colunmOrden)}"

    def padronizar2(self, dados):
        # hashmap/dicionário
        hashLista = {}
        lista = []

        media = np.mean(dados)
        desv_padrao = np.std(dados)

        for i in range(len(dados)-1):
            if hashLista.get(dados[i]):
                lista.append(hashLista[dados[i]])

            else:
                # Formula de padronização:
                valuePadron = (dados[i] - media)/(desv_padrao)

                hashLista[dados[i]] = valuePadron # arredondado para 4 casas decimais
                lista.append(valuePadron)
        
        self.colunmPadron = lista
        self.colunmOrden = lista
        self.colunmOrden.sort()

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

        print(f"{name} exportado com sucesso!")

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
        print("Iniciando o tratamento dos dados...")

        # self.normalizar(colunaY)
        # Ycolunm = self.colunmNorm
        self.padronizar(colunaY)
        Ycolunm = self.colunmPadron
        campoY = self.campo

        self.ajusteMedia(colunaX)
        # self.normalizar2(self.campo)
        # Xcolunm = self.colunmNorm
        self.padronizar2(self.campo)
        Xcolunm = self.colunmPadron
        campoX = self.campo

        print("Normalização completa.")

        # self.padronizar(colunaY)
        # Ycolunm = self.colunmPadron
        # self.padronizar(colunaX)
        # Xcolunm = self.colunmPadron
        # print("Padronização completa.")

        print("Iniciando ajuste polinomial...")

        x = np.array(Xcolunm)
        y = np.array(Ycolunm)

        # x = np.array(campoX)
        # y = np.array(campoY)

        # x.sort()
        # y.sort()s

        def func(x, a, b, c, d):
            return a*x**3 + b*x**2 + c*x + d

        popt, pcov = curve_fit(func, x, y)

        ## Cálculo do R-quadrado
        print("Calculando o R-quadrado...")

        media = np.mean(y)
        # print(f"media y: {media}")

        y_fit = func(x, *popt)

        ## Soma dos Quadrados dos Resíduos (SSres)
        ss_res = np.sum((y - y_fit) ** 2)
        # print(f"SSres: {ss_res}")

        ## Soma dos Quadrados Explicada (SSreg)
        ss_reg = np.sum((y_fit - media)**2)
        # print(f"SSreg: {ss_reg}")
        
        ## Soma Total dos Quadrados (SStot)
        ss_tot = np.sum((y - media) ** 2)
        # print(f"SStot: {ss_tot}")

        ## R-quadrado
        r2 = (ss_reg / ss_tot)
        r2 = 1 - (ss_res / ss_tot)
        print(f"R-quadrado: {r2:.3f}")

        # r2 = r2_score(y_fit, y)
        # print(f"O R-quadrado: {r2:.3f}")

        print("Ajuste completo!")

        ## Iniciando o plot
        plt.style.use('ggplot')
        fig, ax = plt.subplots()

        #legenda = f'%5.6f x³ + %5.6f x² + %5.6f x + %5.6f\n{r2:.4f}' %tuple(popt)
        legenda = f'x3=%5.6f\nx2=%5.6f\nx1=%5.6f\nx0=%5.6f\nR² = {r2:.4f}' %tuple(popt)
        # legenda = "f(x) = ax³ + bx² + cx + d"
        
        plt.grid(True)
        plt.plot(x, y, '*')
        plt.plot(x, func(x, *popt), label=legenda)
        plt.legend(fontsize=12, frameon=True, framealpha=0.7, facecolor='white')
        # textstr = 'a=%5.4f\nb=%5.4f\nc=%5.4f\nd=%5.4f' %tuple(popt)
        textstr = f'X0 = {self.delta%5.3f}'
        ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=10, verticalalignment='top')        

        plt.title('Ajuste polinomial de grau 3')

        # Plot dos campos elétricos
        plt.style.use('ggplot')
        plt.figure(figsize=(8,5))
        plt.title(f'Campo elétrido', fontsize=16, fontweight='bold', fontfamily='monospace')
        plt.xlabel('tempo', fontsize=10, fontfamily='monospace')
        plt.ylabel('V/m', fontsize=10, fontfamily='monospace')
        plt.plot(campoX, label="fm0233")
        plt.plot(campoY, label="fm0211")
        plt.legend(fontsize=12, frameon=True, framealpha=0.7 , facecolor='white')
        
        plt.show()

    def ajustePol1(self, colunaX, colunaY):
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
        ss_res = np.sum((x - y) ** 2)
        print(f"SSR: {ss_res}")
        
        # ## Soma Total dos Quadrados (TSS)
        media = np.mean(y)
        ss_tot = np.sum((y - media) ** 2)
        print(f"TSS: {ss_tot}")

        # ## R-quadrado
        r2 = 1 - (ss_res / ss_tot)
        print(f"R-quadrado: {r2:.3f}")

        #
        ## com Sklearn
        #
        #r2 = r2_score(x, y)
        #print(f"O R-quadrado: {r2:.3f}")


        print("Iniciando ajuste polinomial...")

        def func(x, c, d):
            return c*x + d

        popt, pcov = curve_fit(func, x, y)

        print("Ajuste completo!")

        fig, ax = plt.subplots()

        #legenda = f'%5.6f x³ + %5.6f x² + %5.6f x + %5.6f\n{r2:.4f}' %tuple(popt)
        legenda = f'x1=%5.6f\nx0=%5.6f' %tuple(popt)
        # legenda = "f(x) = ax³ + bx² + cx + d"
        
        plt.grid(True)
        plt.plot(x, y, '*')
        plt.plot(x, func(x, *popt), label=legenda)
        plt.legend(fontsize=12, frameon=True, framealpha=0.7, facecolor='white')
        # textstr = 'a=%5.4f\nb=%5.4f\nc=%5.4f\nd=%5.4f' %tuple(popt)

        # ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=10, verticalalignment='top')        

        plt.title('Ajuste polinomial de grau 1')
        plt.show()

    def ajusteMedia(self, coluna):
        mediaRef = self.media

        self.extractColumn(coluna)
        media = self.media

        self.delta = mediaRef - media

        # hashmap/dicionário
        hashLista = {}
        lista = []

        if self.delta < 0:
            for i in range(len(self.campo)):
                if hashLista.get(self.campo[i]):
                    lista.append(hashLista[self.campo[i]])

                else:
                    value = self.campo[i] + self.delta
                    hashLista[self.campo[i]] = value
                    lista.append(value)

        if self.delta > 0:
            for i in range(len(self.campo)):
                if hashLista.get(self.campo[i]):
                    lista.append(hashLista[self.campo[i]])

                else:
                    value = self.campo[i] + self.delta
                    hashLista[self.campo[i]] = value
                    lista.append(value)
        self.campo = lista

    def analise(self, colunaX, colunaY):

        self.trataOutlier2(colunaY)

        print(f"Inciando normalização de {colunaY}")

        # self.normalizar2(self.dadosTratados)
        self.padronizar2(self.dadosTratados)
        # Ycolunm = self.colunmNorm
        # Ycolunm = self.colunmOrden
        Ycolunm = self.colunmPadron

        # mediaG = self.media
        # desv_padrao = self.dp

        # self.trataOutlier(colunaX)
        # self.normalizar2(self.dadosTratados)
        # Xcolunm = self.colunmNorm
        # Xcolunm = self.colunmOrden

        self.extractColumn(colunaX)
        dados = self.campo

        sigma = "\u03c3"
        mu = "\u03bc"

        # media = round(np.mean(dados), 2)
        media = np.mean(dados)
        desv_padrao = np.std(dados)
        cv = (desv_padrao / media) * 100

        print(f"Estatística para: {colunaX}")
        print(f"Média ({mu}): {media:.2f}.")
        print(f"DP {sigma}: {desv_padrao:.2f}.")
        print(f"Coeficiente de variação: {cv:.2f}%.")

        # self.histograma1(dados, coluna)

        # # Método do Devio Padrão
        # valor_corte = desv_padrao * 3
        # valor_superior = media + valor_corte
        # valor_inferior = media - valor_corte

        # idx = np.where((dados < valor_inferior) | (dados > valor_superior) )
        # outliersIndice = idx[0]

        # # print(indices)
        # # print(f"Dados: {len(dados)} pontos")
        # # print(f"Indices outliers: {len(outliersIndice)} pontos")

        # print(f"Substituindo outliers pela média {media}...")

        # for i in outliersIndice:
        #     dados[i] = media

        # Método do Z-score
        z_score = []
        # media = np.mean(dados)
        # desv_padrao = np.std(dados)

        for i in range(len(dados)):
            z_score.append((dados[i] - media)/desv_padrao)

        print(f"Zscore min: {np.min(z_score)}")
        print(f"Zscore max: {np.max(z_score)}")

        dadoTratado = []

        for j in range(len(dados)-1):
            if z_score[j] >= 3 or z_score[j] <= -3:
                dadoTratado.append(media)
            else:
                dadoTratado.append(dados[j])

        dados = dadoTratado

        # print(f"Foram substituídos {len(outliersIndice)} outliers.")

        print(f"Iniciando normalização de {colunaX}")
        # self.normalizar2(dados)
        self.padronizar2(dados)
        # Xcolunm = self.colunmNorm
        # Xcolunm = self.colunmOrden
        Xcolunm = self.colunmPadron

        # self.boxplot1(Xcolunm, colunaX)

        # self.boxplot1(Ycolunm, colunaY)

        print("Iniciando ajuste polinomial...")

        x = np.array(Xcolunm)
        y = np.array(Ycolunm)

        def func(x, a, b, c, d):
            return a*x**3 + b*x**2 + c*x + d

        popt, pcov = curve_fit(func, x, y)

        ## Cálculo do R-quadrado
        print("Calculando o R-quadrado...")

        media = np.mean(y)
        # print(f"media y: {media}")

        y_fit = func(x, *popt)

        # Coeficiente de determinação R2 com Sklearn
        r2 = r2_score(y_fit, y)
        print(f"O R-quadrado: {r2:.3f}")
   

        print("Ajuste completo!")

        # Iniciando o plot

        fig, ax = plt.subplots()

        #legenda = f'%5.6f x³ + %5.6f x² + %5.6f x + %5.6f\n{r2:.4f}' %tuple(popt)
        legenda = f'x3=%5.6f\nx2=%5.6f\nx1=%5.6f\nx0=%5.6f\n R²={r2:.4f}' %tuple(popt)
        # legenda = "f(x) = ax³ + bx² + cx + d"
        
        plt.grid(True)
        plt.plot(x, y, '*')
        plt.plot(x, func(x, *popt), label=legenda)
        plt.legend(fontsize=12, frameon=True, framealpha=0.7, facecolor='white')
        # textstr = 'a=%5.4f\nb=%5.4f\nc=%5.4f\nd=%5.4f' %tuple(popt)

        # ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=10, verticalalignment='top')        

        plt.title('Ajuste polinomial de grau 3')

        # plt.figure()
        # plt.grid(True)
        # plt.plot(y_fit, label="Modelo")
        # plt.plot(y, label="fm0211")
        # plt.legend(fontsize=12, frameon=True, framealpha=1, facecolor='white')
        # plt.title("fm0211 x Modelo")

        plt.show()


        # print('Iniciando o histograma...')

        # plt.subplot(1, 2, 1)
        # plt.hist(Ycolunm, bins=30, color="orange", edgecolor="black")
        # plt.title("Histograma fm0211")
        # plt.xlabel("valor")
        # plt.ylabel("frequência")
        # plt.grid()

        # plt.subplot(1, 2, 2)
        # plt.hist(Xcolunm, bins=30, color="orange", edgecolor="black")
        # plt.title("Histograma fm0233")
        # plt.xlabel("valor")
        # plt.ylabel("frequência")
        # plt.grid()

        # print('Iniciando o boxplot...')
        
        # Agrupando os dados, calculando a média e o desvio padrão:
        # data = [Ycolunm] + [Xcolunm]
        # media = []
        # desv_padrao = []

        # for i in data:
        #     media.append(np.mean(i))
        # for j in data:
        #     desv_padrao.append(np.std(j))

        # plt.figure()
        # plt.boxplot(data, positions=[1, 2], labels=['fm0211', 'fm0233'], boxprops=dict(color='blue'), whiskerprops=dict(color='red'), capprops=dict(color='green'), medianprops=dict(color='orange'), flierprops=dict(markerfacecolor='white', marker='o'))

        # # Configurando a média com pontos vermelhos:
        # for i in range(len(media)):
        #     plt.plot(i + 1, media[i], 'ro')
        
        # # Adionando desvio padrão com barras de erro:
        # for i in range(len(desv_padrao)):
        #     plt.errorbar(i + 1, media[i], yerr=desv_padrao[i], fmt='o', color='red')
        
        # # Outras configurações do gráfico:
        # plt.title('Boxplot Agrupado')
        # plt.ylabel('valores')
        # plt.show()

    def trataOutlier(self, coluna):
        print("Iniciando tratamento de outliers...")

        self.extractColumn(coluna)
        dados = self.campo

        sigma = "\u03c3"
        mu = "\u03bc"

        media = round(np.mean(dados), 2)
        desv_padrao = np.std(dados)
        cv = (desv_padrao / media) * 100

        print(f"Estatística para: {coluna}")
        print(f"Média ({mu}): {media:.2f}.")
        print(f"DP {sigma}: {desv_padrao:.2f}.")
        print(f"Coeficiente de variação: {cv:.2f}%.")

        # self.histograma1(dados, coluna)

        # Método do Devio Padrão
        valor_corte = desv_padrao * 3
        valor_superior = media + valor_corte
        valor_inferior = media - valor_corte

        idx = np.where((dados < valor_inferior) | (dados > valor_superior) )
        outliersIndice = idx[0]

        # print(indices)
        # print(f"Dados: {len(dados)} pontos")
        # print(f"Indices outliers: {len(outliersIndice)} pontos")
        print(f"Substituindo outliers pela média {media}...")
        for i in outliersIndice:
            dados[i] = media

        print(f"Foram substituídos {len(outliersIndice)} outliers.")

        self.dadosTratados = dados
        # self.media = media
        # self.dp = desv_padrao

        # print(f"Dados sem outliers: {len(dados)} pontos")

        # self.boxplot1(dados, coluna)
    
    def trataOutlier2(self, coluna):
        print("Iniciando tratamento de outliers...")

        self.extractColumn(coluna)
        dados = self.campo

        sigma = "\u03c3"
        mu = "\u03bc"

        media = np.mean(dados)
        desv_padrao = np.std(dados)
        cv = (desv_padrao / media) * 100

        print(f"Estatística para: {coluna}")
        print(f"Média ({mu}): {media:.2f}.")
        print(f"DP {sigma}: {desv_padrao:.2f}.")
        print(f"Coeficiente de variação: {cv:.2f}%.")

        # self.histograma1(dados, coluna)

        # Método do Z-score
        z_score = []
        media = np.mean(dados)
        desv_padrao = np.std(dados)

        for i in range(len(dados)-1):
            z_score.append((dados[i] - media)/desv_padrao)

        print(f"Zscore min: {np.min(z_score)}")
        print(f"Zscore max: {np.max(z_score)}")

        dadoTratado = []

        for j in range(len(dados)-1):
            if z_score[j] >= 3 or z_score[j] <= -3:
                dadoTratado.append(media)
            else:
                dadoTratado.append(dados[j])

        # print(indices)
        # print(f"Dados: {len(dados)} pontos")
        # print(f"Indices outliers: {len(outliersIndice)} pontos")
        # for i in outliersIndice:
        #     dados[i] = media

        self.dadosTratados = dadoTratado

        # print(f"Dados sem outliers: {len(dados)} pontos")

        # self.boxplot1(dados, coluna)

    def boxplot1(self, dados, nome):
        media = np.mean(dados)
        desv_padrao = np.std(dados)

        plt.figure()
        plt.boxplot(dados, positions=[1], labels=[f'{nome}'], boxprops=dict(color='blue'), whiskerprops=dict(color='red'), capprops=dict(color='green'), medianprops=dict(color='orange'), flierprops=dict(markerfacecolor='white', marker='o'))

        # Configurando a média com pontos vermelhos:
        plt.plot(1, media, 'ro')
        
        # Adionando desvio padrão com barras de erro:
        plt.errorbar(1, media, yerr=desv_padrao, fmt='o', color='red')
        
        # Outras configurações do gráfico:
        plt.title('Boxplot')
        plt.ylabel('valores')
        plt.show()

    
    def histograma1(self, dados, coluna):
        nome = coluna
        plt.figure()
        plt.hist(dados, bins=30, color="orange", edgecolor="black")
        plt.title(f"Histograma {nome}")
        plt.xlabel("valor")
        plt.ylabel("frequência")
        plt.grid()
        plt.show()

    def histograma2(self, colunaX, colunaY):
        self.extractColumn(colunaX)
        Xcampo = self.campo

        self.extractColumn(colunaY)
        Ycampo = self.campo

        plt.subplot(1, 2, 1)
        plt.hist(Ycampo, bins=30, color="orange", edgecolor="black")
        plt.title("Histograma fm0211")
        plt.xlabel("valor")
        plt.ylabel("frequência")
        plt.grid()

        plt.subplot(1, 2, 2)
        plt.hist(Xcampo, bins=30, color="orange", edgecolor="black")
        plt.title("Histograma fm0233")
        plt.xlabel("valor")
        plt.ylabel("frequência")
        plt.grid()

        plt.figure()
        plt.boxplot(Ycampo)
        plt.title('Boxplot campo fm0211')

        plt.figure()
        plt.boxplot(Xcampo)
        plt.title('Boxplot campo fm0233')

        plt.show()


    def plotarPulsos(self, coluna):
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
    
    def plotar(self, coluna):
        self.extractColumn(coluna)

        # configurações de plotagem
        ## padrão de estilo
        plt.style.use('ggplot')
        plt.figure(figsize=(8,5))

        plt.title(f'Campo elétrido de {coluna}', fontsize=16, fontweight='bold', fontfamily='monospace')
        plt.xlabel('tempo', fontsize=10, fontfamily='monospace')
        plt.ylabel('V/m', fontsize=10, fontfamily='monospace')

        tempo = list(range(len(self.campo)))
        # plt.scatter(tempo, self.campo)
        plt.plot(self.campo)
        plt.legend(fontsize=12, frameon=True, framealpha=0.7 , facecolor='white')
        
        return plt.show()

    def plotContra(self, colunaX, colunaY):
        # self.normalizar(colunaX)
        self.padronizar(colunaX)
        # Xcolunm = self.colunmNorm
        Xcolunm = self.colunmPadron
        # Xcolunm = self.colunmOrden
        # Xcolunm = self.campo
        print(f"o tamanho de X é {len(Xcolunm)}")

        # self.normalizar(colunaY)
        self.padronizar(colunaY)
        # Xcolunm = self.colunmNorm
        Ycolunm = self.colunmPadron
        # Ycolunm = self.colunmOrden
        # Ycolunm = self.campo
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
        # plt.scatter(Xcolunm, Ycolunm, label="combinação.")
        plt.plot(Xcolunm, Ycolunm, label="combinação.")
        plt.legend(fontsize=12, frameon=True, framealpha=0.7 , facecolor='white')
        
        return plt.show()

