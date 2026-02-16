from collections import defaultdict
from dataclasses import dataclass, field

sizes = ["XS", "S", "M", "L", "XL", "XXL"]

@dataclass
class Queue:
    Q: list = field(default_factory=list)

    def dequeue(self):
        return self.Q.pop(0)
    def enqueue(self, num):
        self.Q.append(num)
    def size(self):
        return len(self.Q)

class Graph:
    capacidade: defaultdict
    vertices: list

    def __init__(self, n_camisas:int, n_pessoas:int, preferencias:dict):
        self.capacidade = defaultdict(lambda: defaultdict(str))
        self.vertices = ["i"] +  sizes + [str(i) for i in range(1, n_pessoas + 1)] + ["f"]

        for size in sizes:
            self.capacidade["i"][size] = n_camisas // 6
            self.capacidade[size]["i"] = 0
            for j in range(1, n_pessoas + 1):
                self.capacidade[size][str(j)] = 0
                self.capacidade[str(j)][size] = 0
                self.capacidade[str(j)]["f"] = 1
                self.capacidade["f"][str(j)] = 0

        for i in range(1, n_pessoas + 1):
            self.capacidade[preferencias[i][0]][str(i)] = 1
            self.capacidade[str(i)][preferencias[i][0]] = 0
            self.capacidade[preferencias[i][1]][str(i)] = 1
            self.capacidade[str(i)][preferencias[i][1]] = 0
    
    def __bfs(self):
        visitado = {}
        pai = {}

        for u in self.vertices:
            visitado[u] = False
            pai[u] = None

        visitado["i"] = True
        Q = Queue()
        Q.enqueue("i")

        while Q.size() != 0:
            u = Q.dequeue()
            for v in self.capacidade[u]:
                if self.capacidade[u][v] > 0 and not visitado[v]:
                    visitado[v] = True
                    pai[v] = u
                    Q.enqueue(v)

                    if v == "f":
                        return True, pai

        return False, None

    def FordFulkerson(self) -> int:
        fluxo_maximo = 0

        while True:
            existe_caminho_aumentador, pai = self.__bfs()
            if not existe_caminho_aumentador:
                break
            capacidade_residual = float("inf")
            atual = "f"
            while atual != "i":
                capacidade_residual = min(capacidade_residual, self.capacidade[pai[atual]][atual])
                atual = pai[atual]
            
            fluxo_maximo += capacidade_residual
            
            atual = "f"
            while atual != "i":
                self.capacidade[pai[atual]][atual] -= capacidade_residual
                self.capacidade[atual][pai[atual]] += capacidade_residual
                atual = pai[atual]

        return fluxo_maximo

    
instancias = int(input())
for _ in range(instancias):
    n_camisas, n_pessoas = map(int, input().split())
    preferencias = {}
    for i in range(1, n_pessoas + 1):
        preferencias[i] = tuple(input().split())
    graph = Graph(n_camisas, n_pessoas, preferencias)
    fluxo_maximo = graph.FordFulkerson()
    print("YES" if fluxo_maximo >= n_pessoas else "NO")