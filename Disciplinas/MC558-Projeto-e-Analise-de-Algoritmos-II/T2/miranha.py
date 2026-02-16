from math import sqrt
# import heapq

def makeset(pontos):
    conjuntos = []
    for ponto in pontos:
        conjuntos.append({ponto})
    return conjuntos

def findset(v, conjuntos):
    for conjunto in conjuntos:
        if v in conjunto:
            return conjunto
    return None

def union(vertices, conjuntos):
    conjuntos.append(findset(vertices[0], conjuntos) | findset(vertices[1], conjuntos))
    conjuntos.remove(findset(vertices[0], conjuntos))
    conjuntos.remove(findset(vertices[1], conjuntos))
    return conjuntos

def kruskal(vertices, distancias):

    conjuntos = makeset(vertices)
    comprimento = 0

    w = dict(sorted(distancias.items(), key=lambda item: item[1]))

    # items = list(distancias.items())
    # w = heapq.nsmallest(len(items), items, key=lambda item: item[1])
    # w = dict(w)

    for vertices, e in w.items():
        if findset(vertices[0], conjuntos) != findset(vertices[1], conjuntos):
            conjuntos = union(vertices, conjuntos)
            comprimento += e

    return comprimento

instancias = int(input())
dist = lambda p1, p2: sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

for _ in range(instancias):
    vertices = []
    n_pessoas = int(input())
    [vertices.append(tuple(map(int, input().split()))) for _ in range(n_pessoas)]
    distancias = {(u, v): dist(u, v) for u in vertices for v in vertices if u != v}
    print(f'{kruskal(vertices, distancias)/100:.2f}')