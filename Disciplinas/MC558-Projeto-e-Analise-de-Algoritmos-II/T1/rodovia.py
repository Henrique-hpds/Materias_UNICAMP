import sys

def dfs_visit(u:int, adj:dict, cor:dict):
    cor[u] = "c"
    for v in adj[u]:
        if u != v and cor[v] == "b":
            dfs_visit(v, adj, cor)
    cor[u] = "p"

def dfs(adj:dict):
    cor = {}
    n_componentes = 0
    for u in adj.keys():
        cor[u] = "b"
    for u in adj.keys():
        if cor[u] == "b":
            dfs_visit(u, adj, cor)
            n_componentes += 1
    if n_componentes == 1:
        return True
    return False

sys.setrecursionlimit(200000) 
cidades = int(input())
adj = {}

for i in range(1, cidades + 1):
    adj[i] = []

for _ in range(cidades):
    i, j = map(int, input().split())
    adj[i].append(j)

adj_trans = {v: [] for v in adj.keys()}
for u, vizinhos in adj.items():
    for v in vizinhos:
        adj_trans[v].append(u)

if dfs(adj) and dfs(adj_trans):
    print("S")
else:
    print("N")