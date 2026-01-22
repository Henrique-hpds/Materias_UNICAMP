import matplotlib.pyplot as plt
from math import *
from numpy import linspace, cos, sin

cor = ['#fcfc81', '#e6f2a2', '#d4ffff', '#a5a391',  '#ba9e88',  '#598556', '#65ab7c', '#a6c875', '#a7ffb5', '#05ffa6', '#0cb577', '#23c48b', '#017374', '#1f6357', '#214761', '#734a65', '#3778bf', '#3c73a8', '#4b57db', '#021bf9', '#0c06f7', '#533cc6', '#894585', '#DC143C', '#B22222',  '#A52A2A', '#800000','#FF0000', '#952e8f', '#ff0789', '#ff6163', '#e78ea5',  '#d99b82', '#ccad60', '#efb435', '#c2b709', '#8fae22', '#9bb53c', '#70b23f', '#388004', '#a8ff04', '#d90166', '#69d84f','#015482',  '#b2996e', '#61de2a', '#DB3069', '#484A47', '#B0DB43', '#12EAEA', '#BCE7FD', '#CADBC0', '#E3D8F1', '#14342B', '#304C89', '#FFEE88', '#2CF6B3', '#F77F00']

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])


def plota_grafico(pontos: list, erro:float) -> None:
    

    plt.xlabel("Eixo x (cm)")
    plt.ylabel("Eixo y (cm)")
    plt.title("Curvas de Nível de Tensão")
    
    coluna_x = list()
    coluna_y = list()
    
    menor = pontos[0].ddp
    i = 0
    for atual in pontos:
        if atual.ddp - menor <= erro * 2:
            coluna_x.append(atual.coordenada["x"])
            coluna_y.append(atual.coordenada["y"])
        else:
            plt.scatter(coluna_x, coluna_y, label= truncate((menor + erro), 2) + ' V ± ' + truncate(erro, 2), c=cor[i], marker='o') #markeredgecolor=cor , markerfacecolor="black", markersize=2,marker="o"
            menor = atual.ddp 
            coluna_x.clear()
            coluna_y.clear()
            coluna_x.append(atual.coordenada["x"])
            coluna_y.append(atual.coordenada["y"])  
            i+=1    

    angle = linspace( 0 , 2 * pi , 1500 ) 
 
    radius = 2
    
    # x = radius * cos( angle ) 
    # y = radius * sin( angle ) 
    # plt.scatter(x + 15, y + 10, s=2., c='black')
    

    

    # plt.legend(bbox_to_anchor=(1.01, 1.2), loc='upper left')
    plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', ncol=2)
    plt.show()


# X11:hotpink mediumvioletred fuchsia m darkmagenta indigo rebeccapurple darkslateblue mediumblue midnigthblue slategray darkcyan darkgreen goldenrod darkgoldenrod darkorange orangered r maroon brown grey k'

