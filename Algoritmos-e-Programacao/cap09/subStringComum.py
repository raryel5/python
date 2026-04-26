palavra_a = ["f", "i", "s", "h"]
palavra_b = ["h", "i", "s", "h"]

#celula = 


for i in range(len(palavra_a)):
    if palavra_a[i] == palavra_b[j]:
    celula[i][j] = celula[i-1][j-1] + 1
    else:
        celula[i][j] = 0