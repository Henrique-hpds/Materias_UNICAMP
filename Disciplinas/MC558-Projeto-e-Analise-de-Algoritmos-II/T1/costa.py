l, c = [int(i) for i in input().split()]
matrix = [[j for j in input()] for _ in range(0, l)]
adj = 0

for i in range(0, l):
    for j in range(0, c):
        if matrix[i][j] == '#':
            cont = 0
            try:
                if matrix[i][j-1] == '#':
                    cont += 1
            except:
                cont += 1
            try:
                if matrix[i][j+1] == '#':
                    cont += 1
            except:
                cont += 1
            try:
                if matrix[i-1][j] == '#':
                    cont += 1
            except:
                cont += 1
            try:
                if matrix[i+1][j] == '#':
                    cont += 1
            except:
                cont += 1

            if cont != 4:
                adj += 1
print(adj)