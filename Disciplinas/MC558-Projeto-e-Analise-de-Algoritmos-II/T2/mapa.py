def makeset(pontos):
    conjuntos = []
    for ponto in pontos:
        conjuntos.append({ponto})
    return conjuntos

def findset(v):
    for conjunto in conjuntos:
        if v in conjunto:
            return conjunto
    return None

def union(vertices):
    conjuntos.append(findset(vertices[0]) | findset(vertices[1]))
    conjuntos.remove(findset(vertices[0]))
    conjuntos.remove(findset(vertices[1]))
    return conjuntos

def kruskal(arestas):
    comprimento = 0
    
    w = dict(sorted(arestas.items(), key=lambda item: item[1]))

    for vertices, e in w.items():
        if findset(vertices[0]) != findset(vertices[1]):
            conjuntos = union(vertices)
            comprimento += e

    return comprimento

cidades, rodovias = map(int, input().split())
vertices = [i for i in range(1, cidades + 1)]
arestas = {(i, j): c for i, j, c in [map(int, input().split()) for _ in range(rodovias)]}

conjuntos = makeset(vertices)
print(f'{kruskal(arestas)}')