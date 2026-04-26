# bluble sort
lista = [3, 5, 8, 4, 2, 42, 25, 11]
count = 0

for j in range(len(lista)-1):
    for i in range(len(lista)-1-j):
        if lista[i] > lista[i+1]:
            a = lista[i+1]
            lista[i+1] = lista[i]
            lista[i] = a
        count += 1

print(lista)
print(count)