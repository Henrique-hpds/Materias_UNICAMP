import sys
from dataclasses import dataclass, field

@dataclass
class Queue:
    Q: list = field(default_factory=list)

    def dequeue(self):
        return self.Q.pop(0)
    def enqueue(self, num):
        self.Q.append(num)
    def size(self):
        return len(self.Q)

def dfs_visit(u:int, adj:dict, cor:dict, pai:dict, lista_final:list, tempo:int, d:dict, f:dict):
    cor[u] = "c"
    tempo += 1
    d[u] = tempo
    for v in adj[u]:
        if cor[v] == "b":
            pai[v] = u
            if not dfs_visit(v, adj, cor, pai, lista_final, tempo, d, f):
                return False   
        elif cor[v] == "c":
            return False
    cor[u] = "p"
    tempo += 1
    f[u] = tempo
    lista_final.append(u)     
    return True       

def dfs(adj:dict, lista_final:list):
    cor = {}
    pai = {}
    d = {}
    f = {}
    tempo = 0
    for u in adj.keys():
        cor[u] = "b"
        pai[u] = None
    for u in adj.keys():
        if cor[u] == "b":
            if not dfs_visit(u, adj, cor, pai, lista_final, tempo, d, f):
                return -1
    return 0

# def bfs(adj:dict):
#     cor = {}
#     pai = {}
#     d = {}
#     for u in adj.keys():
#         cor[u] = "b"
#         pai[u] = None
#         d[u] = float("inf")
#     cor[1] = "c"
#     d[1] = 0
#     Q = Queue()
#     Q.enqueue(1)
#     while Q.size() != 0:
#         u = Q.dequeue()
#         for v in adj[u]:
#             if cor[v] == "b":
#                 cor[v] = "c"
#                 d[v] = d[u] + 1
#                 pai[v] = u
#                 Q.enqueue(v)
#         cor[u] = "p"
    

def topological_sort(adj:dict):
    lista_final = []

    # adj_inv = {v: [] for v in adj.keys()}
    # for u, vizinhos in adj.items():
    #     for v in vizinhos:
    #         adj_inv[v].append(u)

    if dfs(adj, lista_final) == -1:
        print(-1)
    else:
        print(len(lista_final) - 1)
    
adj = {}
comecou = False
cont = 1

for linha in sys.stdin:
    if not comecou:
        comecou = True
        n_arquivos = int(linha)
        continue
    if cont < n_arquivos + 1:
        adj[cont] = list(map(int, linha.strip().split()[1:]))
        cont += 1
        if cont == n_arquivos + 1:
            topological_sort(adj)
            comecou = False
            cont = 1
            adj = {}