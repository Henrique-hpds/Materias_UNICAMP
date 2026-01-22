from math import log, e

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

def main():
    continuar = True
    while continuar:
        entrada = input("Precisa linearizar(y/n)?: ")
        if entrada == "y":
            entrada_2 = input("Vai usar ln(y/n)?: ")
            if entrada_2 == "y":
                base = e
            elif entrada_2 == "n":
                base = float(input("Base para linearizar: "))
        
        
        entrada_2 = input("x tem incerteza(y/n)?: ")
        if entrada_2 == "y":
            print("Fudeu, não terminei o programa!")
            entrada_2 = input("São iguais(y/n)?: ")
            if entrada_2 == "n":
                incertezas_x = input("Listas incertezas x: ").split()
                incertezas_x = [float(x) for x in incertezas_x]
            elif entrada_2 == "y":
                incerteza_x = float(input("Incerteza x: "))
            
        entrada_3 = input("y tem incerteza(y/n)?: ")
        if entrada_3 == "y":
            entrada_3 = input("São iguais(y/n)?: ")
            if entrada_3 == "n":
                print("Fudeu, não terminei o programa!")
                incertezas_y = input("Listas incertezas y: ").split()
                incertezas_y = [float(y) for y in incertezas_y]
            elif entrada_3 == "y":
                incerteza_y = float(input("Incerteza y: "))
        
        
        lista_x = input("Lista x: ").split()
        lista_x = [float(x) for x in lista_x]
        
        lista_y = input("Lista y: ").split()
        lista_y = [float(y) for y in lista_y]
        
        if entrada == "y":
            y_linearizado = [log(y, base) for y in lista_y]
            lista_y = y_linearizado
    
        somatorio_x = somatorio_simples(lista_x)
        somatorio_y = somatorio_simples(lista_y)
        
        somatorio_x_quadrado = somatorio_n(lista_x, lista_x)
        somatorio_xy = somatorio_n(lista_x, lista_y)
    
        N = len(lista_x)
        
        delta = Delta(somatorio_x, somatorio_x_quadrado, N)
        
        a = determina_a(N, somatorio_xy, somatorio_x, somatorio_y, delta)
        b = determina_b(somatorio_y, somatorio_x_quadrado, somatorio_xy, somatorio_x, delta)
        
        if entrada_3 == "y":
            incerteza_a = incerteza_y * (N/delta)**0.5
            incerteza_b = incerteza_y * (somatorio_x_quadrado/delta)**0.5
        if delta == 0.0:
            print(f'\n{"_"*30} \n* ATENÇÃO!')
            print("ERRO: ∆ igual a 0!\n")
            print("TENTE NOVAMENTE:\n")
    
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
                
            if entrada == "y":
                print(f'{"_"*30}')
                print("Exponencial: y = ab^(cx)")
                print(f'a = {base**b}')
                if base == e:
                    print(f'b = e')
                else:
                    print(f'b = {base}')
                print(f'c = {a}\n')
    
            else:
                print(f'{"_"*30}')
                print("Reta: y = ax + b")
                print(f'{a = }')
                print(f'{b = }\n')
                
                if entrada_3 == "y":
                    print(f'{incerteza_a = }')
                    print(f'{incerteza_b = }')
                
                print(f'{"_"*30} \n*CASO b = 0:')
                print("a:", somatorio_xy/somatorio_x_quadrado, "\n")
    

            continuar = False
    
if __name__ == '__main__':
    main()
