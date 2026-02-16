def InitializeSingleSource(vertices, s, d, pai):
    for v in vertices:
        d[v] = float('inf')
        pai[v] = None
    d[s] = 0

def Relax(u, v, w, d, pai):
    if d[v] > d[u] + w[u][v]:
        d[v] = d[u] + w[u][v]
        pai[v] = u

# def Dijsktra(vertices:list, w, s):
#     d = dict()
#     pai = dict()

#     InitializeSingleSource(vertices, s, d, pai)
    
#     Q = vertices.copy()

#     while Q:
#         u = min(Q, key=lambda v: d[v])
#         Q.remove(u)
#         for v in vertices:
#             if w[u][v] > 0:
#                 Relax(u, v, w, d, pai)

#     return d

def BellmanFord(vertices:list, arestas:list, w, s):
    d = dict()
    pai = dict()

    InitializeSingleSource(vertices, s, d, pai)

    for _ in range(1, len(vertices)):
        for u, v in arestas:
            Relax(u, v, w, d, pai)
            Relax(v, u, w, d, pai)

    return d

        

# while True:
interceções, ruas = map(int, input().split())

arestas = []
vertices = [i for i in range(1, interceções + 1)]
w = [[0 for _ in range(interceções + 1)] for _ in range(interceções + 1)]

for _ in range(ruas):
    i, j, p = map(int, input().split())
    w[i][j] = 100 - p
    w[j][i] = 100 - p
    arestas.append((i, j))

# d = Dijsktra(vertices, w, 1)
# print(f'{d[interceções - 1]:.6f}')
d = BellmanFord(vertices, arestas, w, 1)
print(d)



    