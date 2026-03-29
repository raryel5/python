def Quicksort(array):

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

    return Quicksort(menores) + [pivo] + Quicksort(maiores)


array = [15, 10, 33, 5, 6, 1, 4, 33, 13, 54, 42, 2]
# array = [15, 10, 33, 5]
lista = Quicksort(array)
print(lista)