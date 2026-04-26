grafo = {}

grafo["inicio"] = {"a":2, "b":2}
grafo["a"] = {"c":2, "fim":2}
grafo["b"] = {"a":2}
grafo["c"] = {"b":-1, "fim":2}
grafo["fim"] = {}

infinito = float("inf")

custos = {
    "a":2,
    "b":2,
    "c":infinito,
    "fim":infinito
    }


pais = {
    "a":"inicio",
    "b":"inicio",
    "c":None,
    "fim":None
    }

processados = set()

def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    for nodo in custos:
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo


nodo = ache_no_custo_mais_baixo(custos)

while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nodo
    processados.add(nodo)
    nodo = ache_no_custo_mais_baixo(custos)

print(custos)
print(pais)