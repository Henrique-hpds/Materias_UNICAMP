from pprint import pprint

def InitializeSingleSource(vertices, s, d, pai):
    for v in vertices:
        d[v] = float('inf')
        pai[v] = None
    d[s] = 0

def Relax(u, v, d, pai):
    if d[v] > d[u] + 1:
        d[v] = d[u] + 1
        pai[v] = u

def Dijsktra(adj:dict, vertices:list, s):
    d = dict()
    pai = dict()

    InitializeSingleSource(vertices, s, d, pai)
    
    Q = vertices.copy()

    while Q:
        u = min(Q, key=lambda v: d[v])
        Q.remove(u)
        for v in adj[u]:
            Relax(u, v, d, pai)

    return d

while True:
    tam_grade = int(input())
    if tam_grade == 0:
        break

    adj = {(i, j):[] for i in range(0, tam_grade) for j in range(tam_grade)}
    vertices = [(i, j) for i in range(0, tam_grade) for j in range(tam_grade)]
    
    for j in range(tam_grade):
        linha = [int(p) for p in input().split()]

        for i in range(0, tam_grade):
            n = linha[4 * i]
            s = linha[4 * i + 1]
            w = linha[4 * i + 2]
            e = linha[4 * i + 3]        
            if n == 1:
                adj[(j, i)].append((j - 1, i))
            if s == 1:
                adj[(j, i)].append((j + 1, i))
            if w == 1:
                adj[(j, i)].append((j, i - 1))
            if e == 1:
                adj[(j, i)].append((j, i + 1))

    pprint(adj)

    # casos = int(input())

    # for _ in range(casos):
    #     x0, y0, x1, y1 = map(int, input().split())
    #     d = Dijsktra(adj, vertices, (x0, y0))
    #     print(d[(x1, y1)])
