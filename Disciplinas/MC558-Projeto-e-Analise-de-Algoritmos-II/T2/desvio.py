def InitializeSingleSource(vertices, s, d, pai, visitado):
    for v in vertices:
        d[v] = float('inf')
        pai[v] = None
        visitado.append(False)
    d[s] = 0

def Relax(u, v, d, w, pai):
    if d[v] > d[u] + w[(u, v)]:
        d[v] = d[u] + w[(u, v)]
        pai[v] = u

def Dijsktra(adj:dict, vertices:list, w:dict, s, rota:list):
    d = dict()
    pai = dict()
    visitado = list()

    InitializeSingleSource(vertices, s, d, pai, visitado)
    
    Q = vertices.copy()

    while Q:
        u = min(Q, key=lambda v: d[v])
        Q.remove(u)

        if visitado[u]:
            continue
        visitado[u] = True  

        if u in rota and u != len(rota) - 1:
            d[u] = 0
            for i in range(u, len(rota) - 1):
                d[u] += w[(i, i + 1)]
            continue

        for v in adj[u]:
            Relax(u, v, d, w, pai)

    return d

while True:
    n_cidades, n_estradas, n_cidades_rota, cidade_conserto = map(int, input().split())
    
    if n_cidades == n_estradas == n_cidades_rota == cidade_conserto == 0:
        break

    adj = {i: [] for i in range(0, n_cidades)}
    vertices = [i for i in range(0, n_cidades)]
    w = {}

    for _ in range(n_estradas):
        cidade1, cidade2, peso = map(int, input().split())
        adj[cidade1].append(cidade2)
        adj[cidade2].append(cidade1)
        w[(cidade1, cidade2)] = peso
        w[(cidade2, cidade1)] = peso

    rota = [i for i in range(0, n_cidades_rota)]
    destino_rota = n_cidades_rota - 1

    d = Dijsktra(adj, vertices, w, cidade_conserto, rota)
    
    print(d)
    print(d[destino_rota])
