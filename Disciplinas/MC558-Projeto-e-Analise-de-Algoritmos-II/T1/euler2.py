import random

def gera_grafo_euleriano(n):
    grafo = {i: [] for i in range(1, n+1)}
    vertices = list(range(1, n+1))
    
    while len(vertices) > 1:
        u = random.choice(vertices)
        vertices.remove(u)
        v = random.choice(vertices)
        vertices.remove(v)
        
        grafo[u].append(v)
        grafo[v].append(u)
        
        if len(grafo[u]) % 2 != 0:
            vertices.append(u)
        if len(grafo[v]) % 2 != 0:
            vertices.append(v)
    
    return grafo
    
def dfs_visit(u:int, adj:dict, cor:dict, caminho:list, eh_euleriano:bool):
    cor[u] = "c"
    caminho.append(u)

    if len(adj[u]) % 2 != 0:
        eh_euleriano = False
        return

    for v in adj[u]:
        if u != v and cor[v] == "b":
            caminho.append((u, v))
            dfs_visit(v, adj, cor, caminho, eh_euleriano)
    cor[u] = "p"
    

def dfs(adj):
    cor = {}
    caminho = []
    segunda_vez = False
    eh_euleriano = True

    for u in adj.keys():
        cor[u] = "b"

    for u in adj.keys():
        if cor[u] == "b" and segunda_vez: # Se há mais de um componente, não é euleriano
            eh_euleriano = False
        if cor[u] == "b" and not segunda_vez:
            dfs_visit(u, adj, cor, caminho, eh_euleriano)
            caminho.append([caminho[-1], caminho[0]])
            caminho.append(caminho[0])
            segunda_vez = True
     
    return (True, caminho) if eh_euleriano else (False, None)