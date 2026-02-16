from math import sqrt
import sys

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

def kruskal(pontos):
    comprimento = 0
    
    # cria o vetor de pesos e o ordena
    w = {(p1, p2):sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) for p1 in pontos for p2 in pontos if p1 != p2}
    w = dict(sorted(w.items(), key=lambda item: item[1]))

    for vertices, e in w.items():
        if findset(vertices[0]) != findset(vertices[1]):
            conjuntos = union(vertices)
            comprimento += e

    return comprimento

pontos = []
comecou = False
cont = 1

for linha in sys.stdin:
    if not comecou:
        comecou = True
        n = int(linha)
        continue
    if cont < n + 1:
        pontos.append(tuple(map(int, linha.split())))
        cont += 1
        if cont == n + 1:
            conjuntos = makeset(pontos)
            print(f'{kruskal(pontos):.2f}')
            comecou = False
            cont = 1
            pontos = []
