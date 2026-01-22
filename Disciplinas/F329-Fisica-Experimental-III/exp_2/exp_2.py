from math import pi, sqrt
import pandas as pd
import matplotlib.pyplot as plt
from numpy import linspace

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def somatorio_n(lista_x, lista_y):
    somatorio = 0
    for i in range(len(lista_x)):
        somatorio += lista_x[i] * lista_y[i]
    return somatorio

def somatorio_simples(lista):
    somatorio = 0
    for x in lista:
        somatorio += x
    return somatorio
    
def Delta(somatorio_x, somatorio_x_quadrado, N):
    delta = N * somatorio_x_quadrado - somatorio_x**2
    return delta

def determina_a(N, xy, x, y, delta):
    try:
        a = (N*xy - x*y)/delta
        return a
    except ZeroDivisionError as error:
        return 0
    
def determina_b(y, x_quadrado, xy, x, delta):
    try:
        b = (y*x_quadrado -xy* x)/ delta
        return b
    except ZeroDivisionError as error:
        return 0
    
def incertezasF2(f_quadrado, tipo):
    arquivo = "periodo" + tipo + ".csv"
    
    periodo = pd.read_csv(arquivo)
    periodo = periodo["periodo"]
    
    incertezaPeriodo = 5 / 1000

    incertezasFrequencia = [incertezaPeriodo/(T ** 2) for T in periodo]
    incertezasFrequencia2 = []

    for i in range(len(incertezasFrequencia)):
        incertezasFrequencia2.append(2 * sqrt(f_quadrado[i]) * incertezasFrequencia[i])

    return incertezasFrequencia2

def incertezaCorrente(corrente):
    incerteza = 0.0001/sqrt(2)
    listaIncerteza = []

    for i in range(len(corrente)):
        incertezaExatidao = 0.008 * corrente[i] + 3 * 0.0001
        listaIncerteza.append(sqrt(incertezaExatidao ** 2 + incerteza ** 2))

    return listaIncerteza

def leitura(tipo):
    arquivo = "exp2" + tipo + ".xlsx"
    dados = pd.read_excel(arquivo)

    corrente = dados["corrente"]
    f_quadrado = dados["f_quadrado"]

    incertezasf2 = incertezasF2(f_quadrado, tipo)
    incerteza_Corrente = incertezaCorrente(corrente)

    return [corrente, f_quadrado, incerteza_Corrente, incertezasf2]


def incertezaMl():
    incertezaM = 0.1/sqrt(2)
    incertezaR = 0.005/200
    incertezaL = 0.005/100

    d = 0.595 / 100 #em m
    r = d / 2 #em m
    l = 2.505 / 100 #em m
    m = (5.3 / 1000) 

    return sqrt(((r * m * incertezaR)/2) ** 2 ((l * m * incertezaL)/6)**2 + (( (r/2) ** 2  +  (l**2)/12  ) * incertezaM) **2)

def determinaIncognitas(coeficientes):
    a = coeficientes[0]
    b = coeficientes[1]

    d = 0.595 / 100 #em m
    r = d / 2 #em m
    l = 2.505 / 100 #em m
    
    n_espiras = 140
    mi_zero = 4 * pi * (10 ** (-7))
    ml = (5.3 / 1000)  * (((r/2) ** 2) + ((l**2)/12))

    mi = (a * 4 * (pi**2) * ml * sqrt(125)) / (8 *  mi_zero * n_espiras)
    Bt = (b * 4 * (pi**2) * ml)/mi

    print(f'\n{mi = }')
    print(f'{Bt = }\n')

def plot (coeficientes, dados):
    a = coeficientes[0]
    b = coeficientes[1]

    listaX = dados[0]
    listaY = dados[1]
    incertezasX = dados[2]
    incertezasY = dados[3]

    pontoCentral = (15.10 + 7.88)/2000

    for i in range(len(listaX)):
        plt.errorbar(listaX[i], listaY[i], xerr= incertezasX[i], yerr = incertezasY[i],c='#000000', marker='o')
    x = linspace(min((min(listaX), pontoCentral)), max(max(listaX), pontoCentral), 1500)
    plt.scatter(x, a * x + b, s=0.2, c='red', label= truncate(a, 3) + "X + " + truncate(b, 1))

    plt.legend(bbox_to_anchor=(1.01, 0.5), loc='upper left')

def mmq(listaX, listaY, incertezaX, incertezasY):
    # incerteza_Ml = incerteza_Ml()

    plt.xlabel("Corrente (mA)", size = 12)
    plt.ylabel("Frequencia ao quadrado(Hz²)", size = 12)
    plt.title("FALTA O TITULO")
            
    incerteza_y = 1 #Arrumar

    somatorio_x = somatorio_simples(listaX)
    somatorio_y = somatorio_simples(listaY)
    
    somatorio_x_quadrado = somatorio_n(listaX, listaX)
    somatorio_xy = somatorio_n(listaX, listaY)

    N = len(listaX)
    
    delta = Delta(somatorio_x, somatorio_x_quadrado, N)
    
    a = determina_a(N, somatorio_xy, somatorio_x, somatorio_y, delta)
    b = determina_b(somatorio_y, somatorio_x_quadrado, somatorio_xy, somatorio_x, delta)
    
    incerteza_a = incerteza_y * (N/delta)**0.5
    incerteza_b = incerteza_y * (somatorio_x_quadrado/delta)**0.5

    if delta == 0.0:
        print(f'\n{"_"*30} \n* ATENÇÃO!')
        print("ERRO: ∆ igual a 0!\n")

    else:
        print(f'\n{"_"*30} \n* RESULTADOS:\n')
        print(f'{listaX = }\n')
        print(f'{listaY = }\n')
        print(f'{somatorio_x = }\n')
        print(f'{somatorio_y = }\n')
        print(f'{somatorio_x_quadrado= }\n')
        print(f'{somatorio_xy = }\n')
        print(f'{N = }\n')
        print(f'∆ = {delta}\n')
            
        print(f'{"_"*30}')
        print("Reta: y = ax + b")
        print(f'{a = }')
        print(f'{b = }\n')
            
        print(f'{incerteza_a = }')
        print(f'{incerteza_b = }')

        return [a, b, incerteza_a, incerteza_b]
    
if __name__ == '__main__':
    dados = leitura("")
    coeficientes = mmq(dados[0], dados[1], dados[2], dados[3])
    plot(coeficientes, dados)
    determinaIncognitas(coeficientes);

    dados = leitura("'")
    coeficientes = mmq(dados[0], dados[1], dados[2], dados[3])
    plot(coeficientes, dados)
    plt.show()
    determinaIncognitas(coeficientes);

