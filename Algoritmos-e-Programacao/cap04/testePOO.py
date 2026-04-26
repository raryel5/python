class QuickSorterSimple:
    def sort(self, arr):
        if len(arr) <= 1:
            return arr
            
        else:
            pivo = arr[0]
            menores = [x for x in arr[1:] if x <= pivo]
            maiores = [x for x in arr[1:] if x > pivo]
            return self.sort(menores) + [pivo] + self.sort(maiores)

# Uso
sorter = QuickSorterSimple()
print(sorter.sort([15, 10, 33, 5, 6, 1, 4, 33, 13, 54, 42, 2]))