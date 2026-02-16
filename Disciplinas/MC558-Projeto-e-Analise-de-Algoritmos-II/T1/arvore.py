def dfs(adj):
    visitado = {}
    tamanho_componente = 0
    for u in adj.keys():
        visitado[u] = False
    for u in adj.keys():
        if not visitado[u]:
            dfs_visit(u, adj, visitado)
            tamanho_componente += 1
    print(tamanho_componente)

def dfs_visit(u, adj, visitado):
    visitado[u] = True
    for v in adj[u]:
        if not visitado[v]:
            dfs_visit(v, adj, visitado)
    visitado[u] = True

_, relacoes = map(int, input().split())

adj = {}
jafoi = []

for _ in range(relacoes):
    nome1, _, nome2 = input().split()
    if not nome1 in jafoi:
        adj[nome1] = [nome2]
        jafoi.append(nome1)
    else:
        adj[nome1].append(nome2)

    if not nome2 in jafoi:
        adj[nome2] = [nome1]
        jafoi.append(nome2)
    else:
        adj[nome2].append(nome1)
    
dfs(adj)