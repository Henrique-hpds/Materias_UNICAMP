from ponto import *
from leitura import *
from plot import *

def main():
    pontos = list()

    print("\n\n\tInterpolar Pontos\n\n")

    arquivo = input("Nome do arquivo (com a extensão): ")
    n = int(input("Número de interpolações: "))
    erro = float(input("Qual a incerteza: "))

    ler_dados(pontos, arquivo, n)

    pontos = sorted(pontos, key=lambda ponto: ponto.ddp) 

    plota_grafico(pontos, erro)

if __name__ == "__main__":
    main()

'''Lembrar de testar a simetria'''