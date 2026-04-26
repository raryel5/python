from collections import deque
# 
# pop -> dequeue = desenfileirar
# push -> enqueue = enfileirar
# 
grafo = {}

grafo["Renan"] = ["Alice", "Bob", "Claire"]
grafo["Bob"] = ["Anuj", "Peggy"]
grafo["Alice"] = ["Peggy"]
grafo["Claire"] = ["Thom", "Jonny"]
grafo["Anuj"] = []
grafo["Peggy"] = []
grafo["Thom"] = []
grafo["Jonny"] = []

# Anuj, Peggy, Thom e Jonny são dígrafos ou grafo não direcionado, pois a relação que envolve eles é em apenas um sentido. Ambos os vértices são vizinhos um do outro.

def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'

def pesquisa(nome):
    # Cria uma nova lista.
    fila_de_pesquisa = deque()

    # Adiciona todos os seus vizinhos para a lista de pesquisa.abs 
    fila_de_pesquisa += grafo["Renan"]

    # Esse vetor é a forma pela qual você mantém o registro das pessoas que já foram verificadas
    verificadas = []


    # Enquanto a fila não estiver vazia ...
    while fila_de_pesquisa:
        # … pega a primeira pessoa da fila
        pessoa = fila_de_pesquisa.popleft()

        # Verifica essa pessoa somente se ela já não tiver sido verificada.
        if not pessoa in verificadas:
            # Verifica se essa pessoa é uma vendedora de mangas
            if pessoa_e_vendedor(pessoa):
                # Sim, ela é uma vendedora de mangas.
                print(pessoa + " é um vendedor de manga.")
            else:
                # Não, ela não é uma vendedora de mangas. Adiciona todos os amigos dessa pessoa à lista
                fila_de_pesquisa += grafo[pessoa]

                # Marca essa pessoa como verificada.
                verificadas.append(pessoa)

            # Se você chegou até aqui, é sinal de que nenhuma pessoa da fila era uma vendedora de mangas.

pesquisa("Renan")

"""
class Graph:
    def __init__(self, n):
        self.value = n

"""