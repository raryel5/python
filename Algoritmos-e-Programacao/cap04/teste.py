def Quicksort(array):
    if len(array) <= 1:
        return array
            
    else:
        pivo = array[0]
        menores = [x for x in array[1:] if x <= pivo]
        maiores = [x for x in array[1:] if x > pivo]
        return Quicksort(menores) + [pivo] + Quicksort(maiores)

# array = [15, 10, 33, 5, 6, 1, 4, 33, 13, 54, 42, 2]
array = [15, 10, 33, 5]
lista = Quicksort(array)
print(lista)