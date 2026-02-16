while True:
    entrada = input()
    if entrada == '0':
        break
    interceções, ruas = map(int, entrada.split())

    w = [[0 for _ in range(interceções + 1)] for _ in range(interceções + 1)]

    for _ in range(ruas):
        i, j, p = map(int, input().split())
        w[i][j] = p * 1e-2
        w[j][i] = p * 1e-2

    for k in range(1, interceções + 1):
        for i in range(1, interceções + 1):
            for j in range(1, interceções + 1):
                w[i][j] = max(w[i][j], w[i][k] * w[k][j])
    
    print(f'{w[1][interceções] * 1e2:.6f} percent')