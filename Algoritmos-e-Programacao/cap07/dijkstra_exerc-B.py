grafo = {}

grafo["inicio"] = {"a":10}
grafo["a"] = {"b":20}
grafo["b"] = {"c":1, "fim":30}
grafo["c"] = {"a":1}
grafo["fim"] = {}

infinito = float("inf")

custos = {
    "a":10,
    "b":infinito,
    "c":infinito,
    "fim":infinito
    }


pais = {
    "a":"inicio",
    "b":None,
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