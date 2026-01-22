from ponto import *

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def imprimir(matriz):
    '''Imprimi a matriz que contem as ddps'''
    n_colunas = len(matriz)
    n_linhas = len(matriz[0])
    for i in range(n_colunas):
        for j in range(n_linhas):
            if matriz[i][j] == 0:
                print("------", end="\t")
            else:
                print(truncate(matriz[i][j], 4), end="\t")
        print()
        print()
    print()
    print()

def atualiza_original(matriz, matriz_origiral):
    '''Atualiza a matriz_original, classificando os pontos recem gerados como pontos coletados'''

    n_colunas = len(matriz)
    n_linhas = len(matriz[0])

    for i in range(n_colunas):
        for j in range(n_linhas):
            if matriz[i][j]:
                matriz_origiral[i][j] = 1

def coletado(matriz_origiral, i, j):
    '''Indica se o elemento [i][j] da matriz (não a matriz original) é um ponto que foi coletado'''

    return matriz_origiral[i][j]

def proximo(matriz, i, j, k, direcao):
    '''Acha o proximo valor que será interpola, independente se ele esta atras ou na frente, em cima ou embaixo'''

    multuplicador = 1
    if direcao == "j":
        while(0 < (j + k * multuplicador) < len(matriz[0]) and not coletado(matriz, i, j + k * multuplicador)):
            multuplicador += 1

        if 0 < (j + k * multuplicador) < len(matriz[0]):
            return k * multuplicador
        else:
            return 0

    elif direcao == "i":
        while(0 < (i + k * multuplicador) and (i + k * multuplicador) < len(matriz) and not coletado(matriz, i + k * multuplicador, j)):
            multuplicador += 1

        if 0 < (i + k * multuplicador) and (i + k * multuplicador) < len(matriz):
            return k * multuplicador
        else:
            return 0
        


def fazer_media(matriz, matriz_origiral, i, j):
    '''Faz a média (interpola os pontos adjacentes'''

    if coletado(matriz_origiral, i, j):

        # ando na horizontal para 'frente'   
        k = proximo(matriz_origiral, i, j, +1, 'i')
        if k and not coletado(matriz_origiral, i + int(k/2) + 1, j):
            matriz[i + int(k/2)][j] = (matriz[i][j] + matriz[i + k][j])/2
    
        # ando na horizontal para 'tras'       
        k = proximo(matriz_origiral, i, j, -1, 'i')
        if k and not coletado(matriz_origiral, i + int(k/2), j):
            matriz[i + int(k/2)][j] = (matriz[i][j] + matriz[i + k][j])/2

        # ando na vertical para 'cima'
        k = proximo(matriz_origiral, i, j, +1, 'j')
        if k and not coletado(matriz_origiral, i, j + int(k/2) + 1):
            matriz[i][j + int(k/2)] = (matriz[i][j] + matriz[i][j + k])/2 

        # ando na vertical para 'baixo'
        k = proximo(matriz_origiral, i, j, -1, 'j')
        if k and not coletado(matriz_origiral, i, j + int(k/2)):
            matriz[i][j + int(k/2)] = (matriz[i][j] + matriz[i][j + k])/2 


def interpolar(x, y, ddp, n):
    '''Interpola as ddp proximas'''

    x_inicial = x[0]
    i = 0

    while x[i] == x_inicial: #Acha o padrão dos números, quantidade de linha e colunas 
        i+=1
    n_colunas = int(((len(x)/i) * 2)+ 3) 
    n_linhas = int((i * 2) + 3)
    
    matriz = [ [0 for i in range(n_linhas)] for j in range(n_colunas)]
    matriz_origiral = [ [0 for i in range(n_linhas)] for j in range(n_colunas)] #ira informar se o ponto equilavente na matriz 'matriz' é do conjunto de ponto que coletamos

    for i in range(len(x)):
        if ddp[i] > 0: #Se o valor da ddp[i] > 0 indica que coletamos o dado
            matriz[2 * x[i]][2 * y[i]] = ddp[i]
        else:
            matriz[2 * x[i]][2 * y[i]] = 0

    atualiza_original(matriz, matriz_origiral)

    #Aqui teos que decidir quantas vezes interpolamos

    for i in range(n):
        for i in range(n_colunas):
            for j in range(n_linhas):
                fazer_media(matriz, matriz_origiral, i, j)

        atualiza_original(matriz, matriz_origiral)

    #Termina aqui a quantidade de interpolações


    #Limpo as lista que foram recebidas na função
    x.clear()
    y.clear()
    ddp.clear()

    for i in range(n_colunas):
        for j in range(n_linhas):

            if matriz[i][j] > 0: #Texto se a ddp da matriz é um valor real
                ddp.append(matriz[i][j])
                
                if i%2 == 0:
                    x.append(i/2)
                elif i%2 != 0:
                    x.append(float(i/2))

                if j%2 == 0:
                    y.append(j/2)
                elif j%2 != 0:
                    y.append(float(j/2))
