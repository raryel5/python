import function

# Objeto
#yansa2 = function.FunctionsCalc("2026-03-07a09_211e233.csv")
yansa2 = function.FunctionsCalc("yansa2_2026-03-07a09_fm0211e0233.csv")

# Métodos
# yansa2.plotar("fm0211")
# yansa2.plotar("fm0233")

# print(yansa2.normalizar("fm0211"))
# yansa2.plotContra("fm0233", "fm0211")

yansa2.ajustePolinomial("fm0233", "fm0211")
#yansa2.ajustePol1("fm0233", "fm0211")


# yansa2.ajustePolinBruto("fm0233", "fm0211")

# yansa2.correlacaoBruta("fm0233", "fm0211")

# yansa2.correlacaoNormalized("fm0233", "fm0211")

# yansa2.analise("fm0233", "fm0211")

# yansa2.histograma("fm0233", "fm0211")