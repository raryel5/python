n = 100
listaTeste = []

for i in range(n):
	listaTeste.append(i)


def pesquisa_binaria(lista, item):
	baixo = 0
	alto = len(lista) -1

	while baixo <= alto:
		meio = (baixo + alto)/2
		chute = lista[meio]
		if chute == item:
			return meio
		if chute > item:
			return meio - 1
		else:
			baixo = meio + 1
	return None

item = 99

print pesquisa_binaria(listaTeste, item)
