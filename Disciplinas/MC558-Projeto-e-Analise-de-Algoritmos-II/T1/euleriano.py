import random

def gera_grafo_euleriano(n):
    """
    Gera um grafo euleriano com n vértices.
    Um grafo euleriano precisa ter todos os vértices com grau par.
    
    :param n: número de vértices do grafo
    :return: grafo euleriano representado por uma lista de adjacência
    """
    # Inicializar o grafo como um dicionário de listas vazias
    grafo = {i: [] for i in range(1, n+1)}
    
    # Criar uma lista de vértices para garantir que todos terão grau par
    vertices = list(range(1, n+1))
    
    # Continuar conectando vértices até todos terem grau par
    while len(vertices) > 1:
        # Escolher dois vértices aleatórios diferentes
        u = random.choice(vertices)
        vertices.remove(u)
        v = random.choice(vertices)
        vertices.remove(v)
        
        # Conectar os vértices u e v (ou seja, adicionar a aresta u-v)
        grafo[u].append(v)
        grafo[v].append(u)
        
        # Se após a conexão o grau de u ou v for ímpar, adicioná-los de volta
        if len(grafo[u]) % 2 != 0:
            vertices.append(u)
        if len(grafo[v]) % 2 != 0:
            vertices.append(v)
    
    return grafo

def verifica_paridade(adj_list):
    if len(adj_list) == 0:
        return False
    for u in adj_list.keys():
        if len(adj_list[u]) % 2 != 0:
            return False
    return True

def dfs_visit(u:int, adj:dict, cor:dict, caminho:list):
    cor[u] = "c"
    caminho.append(u)
    for v in adj[u]:
        if u != v and cor[v] == "b":
            caminho.append((u, v))
            dfs_visit(v, adj, cor, caminho)
    cor[u] = "p"

def dfs(adj):
    cor = {}
    n_componentes = 0
    caminho = []
    for u in adj.keys():
        cor[u] = "b"
    for u in adj.keys():
        if cor[u] == "b":
            dfs_visit(u, adj, cor, caminho)
            n_componentes += 1
    if n_componentes == 1:
        return True, caminho
    return False, None


# adj = { 1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2, 4], 4: [1, 2, 3]}
adj = gera_grafo_euleriano(10)
# print(adj)
if dfs(adj)[0] and verifica_paridade(adj):
    caminho = dfs(adj)[1]
    caminho.append((caminho[-1], caminho[0]))
    caminho.append(caminho[0])
    print(caminho)
    print("True")
else:
    print("False")


