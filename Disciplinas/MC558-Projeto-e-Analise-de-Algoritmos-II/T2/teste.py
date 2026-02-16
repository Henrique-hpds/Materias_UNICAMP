import heapq

INF = 100000
MAXSIZE = 101010

# Inicializa as listas de visitação e distância
vis = [False] * MAXSIZE
dist = [INF] * MAXSIZE

class Node:
    def __init__(self, u, w):
        self.u = u
        self.w = w
        self.next = None

class Graph:
    def __init__(self, size):
        # Cria uma lista de adjacência de tamanho `size + 1`
        self.adj = [None] * (size + 1)

    def add_edge(self, u, v, w):
        new_node = Node(u, w)
        new_node.next = self.adj[v]
        self.adj[v] = new_node

def dijkstra(graph, start, size):
    global dist, vis
    dist = [INF] * size
    vis = [False] * size
    dist[start] = 0
    queue = [(0, start)]
    
    while queue:
        d, v = heapq.heappop(queue)
        if vis[v]:
            continue
        vis[v] = True
        
        node = graph.adj[v]
        while node:
            to = node.u
            length = node.w
            if dist[v] + length < dist[to]:
                dist[to] = dist[v] + length
                heapq.heappush(queue, (dist[to], to))
            node = node.next

def main():
    while True:
        # Lê a primeira linha de entrada com os parâmetros principais
        n, m, c, k = map(int, input().split())
        
        # Condição de parada: se todos forem zero
        if n == 0 and m == 0 and c == 0 and k == 0:
            break
        
        graph = Graph(n + 1)
        
        # Lê as arestas do grafo
        for _ in range(m):
            a, b, w = map(int, input().split())
            
            if (a >= c and b >= c) or (a < c and b < c and abs(a - b) == 1):
                graph.add_edge(a, b, w)
                graph.add_edge(b, a, w)
            elif a >= c and b < c:
                graph.add_edge(b, a, w)
            elif b >= c and a < c:
                graph.add_edge(a, b, w)
        
        # Executa o algoritmo de Dijkstra a partir do nó inicial `k`
        dijkstra(graph, k, n + 1)
        print(dist[c - 1])

if __name__ == "__main__":
    main()
