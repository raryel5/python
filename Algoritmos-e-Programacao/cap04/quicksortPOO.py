class Ordenador:
    """
    Classe para ordenar listas usando algoritimo quicksort
    """
    # def __init__(self):
    #     self.menores = []
    #     self.maiores = []
        
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

array = [15, 10, 33, 5, 6, 1, 4, 33, 13, 54, 42, 2]
# array = [15, 10, 33, 5]
objetoLista = Ordenador()

print(objetoLista.quicksort(array))
