import pandas as pd                      # Pacote PANDAS para a leitura e manipulação dos dados
import numpy as np                       # Pacote NUMPY usando para manipulação matemática de matrizes
import matplotlib.pyplot as plt          # Importa a função pyplot como plt para gerar os gráficos 
import matplotlib as mpl                 # Usado para alterar as propriedades dos gráficos
mpl.rc('font', size=14)

# importar os dados 
fn = "Circulo"
df = pd.read_csv(fn+".csv")

#define o tamanho do gráfico
fig, ax = plt.subplots(1,1,figsize=[14,9])

# separa os dados em dois vetores referentes aos eixos e uma matriz referente ao potencial
X = np.array(df.iloc[:,0]) #usa a primeira coluna para gerar o eixo-x de posição
Y = df.iloc[:,1:].columns.values.astype(float) #usa a primeira linha para gerar o eixo-y de posição
Z = np.array(df.iloc[:,1:]); #usa o restante da matriz para gerar a distribuição de potencial

# calcula o campo elétrico a partir do potencial define o campoget electric field
dx, dy = np.gradient(-Z)

# Gráfico do Potencial
cs = ax.contourf(Y,X,Z,levels=15) # escala de cores
ax.clabel(cs, inline=1, fontsize=15, fmt='%1.1f', colors='black')

# Gráfico de vetores do campo elétrico superpostos ao potencial
ax.quiver(Y,X,dy,dx,width=0.00075)

# gera duas linhas horizontais referente as posições das placas paralelas
ax.hlines([0, 19],0,29,colors='black',linestyles='--')

# Proriedades dos eixos
ax.set_xlabel('Distância (cm)', fontsize=20)
ax.set_ylabel('Distância (cm)', fontsize=20)
ax.set_title("Experimento - Com gaiola no centro", fontsize=30)

fn_fig = fn
fig.savefig(fn_fig+'.png',transparent=False)