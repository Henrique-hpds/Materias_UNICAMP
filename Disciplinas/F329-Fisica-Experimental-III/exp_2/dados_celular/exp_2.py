from math import pi, sqrt
import pandas as pd
import matplotlib.pyplot as plt
from numpy import linspace
import sys

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

def getF():
    pass



def mmq():
    d = 0.595 / 100 #em m
    r = d / 2 #em m
    l = 2.505 / 100 #em m
    m1 = (5.3 / 1000)  * (((r/2) ** 2) + ((l**2)/12))
    n_espiras = 140
    mi_zero = 4 * pi * (10 ** (-7))

    incetezaPeriodo = 5 / 1000

    plt.xlabel("Corrente (mA)", size = 12)
    plt.ylabel("Frequencia ao quadrado(Hz²)", size = 12)
    plt.title("FALTA O TITULO")
            
    incerteza_y = 1 #Arrumar
    
    dados = pd.read_excel("exp2.xlsx")
    periodo = pd.read_csv("periodo.csv")

    corrente = dados["corrente"]
    f_quadrado = dados["f_quadrado"]
    
    periodo =  periodo["periodo"]   
    incetezaFrequencia = [incetezaPeriodo/(T ** 2) for T in periodo]

    incetezaFrequencia2 = []
    for i in range(len(f_quadrado)):
        incetezaFrequencia2.append(2 * sqrt(f_quadrado[i]) * incetezaFrequencia[i])
    


    corrente = [float(i) for i in corrente]
    f_quadrado = [float(i) for i in f_quadrado]

    lista_x = corrente
    lista_y = f_quadrado

    somatorio_x = somatorio_simples(lista_x)
    somatorio_y = somatorio_simples(lista_y)
    
    somatorio_x_quadrado = somatorio_n(lista_x, lista_x)
    somatorio_xy = somatorio_n(lista_x, lista_y)

    N = len(lista_x)
    
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
        print(f'{lista_x = }\n')
        print(f'{lista_y = }\n')
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

        mi = (a * 4 * (pi**2) * m1 * sqrt(125)) / (8 *  mi_zero * 140)
        Bt = (b * 4 * (pi**2) * m1)/mi
        print(f'\n{mi = }')
        print(f'{Bt = }\n')


        plt.scatter(lista_x, lista_y, c='#000000', marker='o')
        print(max(lista_x))
        x = linspace(((15.10 + 7.88)/2000), max(lista_x), 1500)
        plt.scatter(x, a * x + b, s=0.2, c='red', label= truncate(a, 3) + "X + " + truncate(b, 1))

    ###############################

    dados = pd.read_excel("exp2'.xlsx")


    corrente = dados["corrente"]
    f_quadrado = dados["f_quadrado"]

    corrente = [float(i) for i in corrente]
    f_quadrado = [float(i) for i in f_quadrado]

    lista_x = corrente
    lista_y = f_quadrado

    somatorio_x = somatorio_simples(lista_x)
    somatorio_y = somatorio_simples(lista_y)
    
    somatorio_x_quadrado = somatorio_n(lista_x, lista_x)
    somatorio_xy = somatorio_n(lista_x, lista_y)

    N = len(lista_x)
    
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
        print(f'{lista_x = }\n')
        print(f'{lista_y = }\n')
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

        mi = -(a * 4 * (pi**2) * m1 * sqrt(125)) / (8 *  mi_zero * 140)
        Bt = (b * 4 * (pi**2) * m1)/mi
        print(f'\n{mi = }')
        print(f'{Bt = }\n')

        # plt.scatter(lista_x, lista_y, c='#000000', marker='o')
        plt.errorbar(lista_x, lista_y, xerr=0.02, yerr=0)
        x = linspace(min(lista_x),((15.10 + 7.88)/2000) ,1500)
        plt.scatter(x, a * x + b, s=0.2, c='blue', label= truncate(a, 3) + "X + " + truncate(b, 1))
        

    plt.legend(bbox_to_anchor=(1.01, 0.5), loc='upper left')
    plt.show()
            
    
if __name__ == '__main__':
    mmq()

