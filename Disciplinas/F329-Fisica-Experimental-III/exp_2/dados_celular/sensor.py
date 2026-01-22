from math import pi, sqrt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dadosN = pd.read_csv("sensor'.csv")
dadosO = pd.read_csv("sensor.csv")

xNormal = dadosN["Bx"]
xOposto = dadosO["Bx"]

yNormal = dadosN["By"]
yOposto = dadosO["By"]

xSolucao = []
ySolucao = []

sist = np.array([[1, 1], [-1, 1]])

somaX =[np.array([41, 2])]
somaY =[np.array([1, 5])]

for i in range(len(dadosN)):
    for j in range(len(dadosO)):
        somaX.append(np.array([xNormal[i], xOposto[j]]))
        somaY.append(np.array([yNormal[i], yOposto[j]]))

for i in range(len(somaX)):
    xSolucao.append(np.linalg.solve(sist, somaX[i]))
    ySolucao.append(np.linalg.solve(sist, somaY[i]))

campoH = []
for i in range(len(xSolucao)):
    # print(str(i) + ": Xt: " + str(xSolucao[i][0]) + ": Yt: + " + str(ySolucao[i][0]) + " Total: " + str(sqrt((xSolucao[i][0]) ** 2 + (ySolucao[i][0])**2)) + '\n')
    campoH.append(sqrt((xSolucao[i][0]) ** 2 + (ySolucao[i][0])**2))

print("Media = " , np.mean(campoH))
print("Desvio = " , np.std(campoH))

desvpada = np.std(campoH)/sqrt(len(xSolucao))
print("Incerteza Estatística =", desvpada)