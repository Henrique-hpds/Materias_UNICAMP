from pulp import *

# Hectares de recursos
milho = LpVariable("milho", lowBound=0, cat='Integer')
soja = LpVariable("soja", lowBound=0, cat='Integer')
trigo = LpVariable("trigo", lowBound=0, cat='Integer')

problema = LpProblem("MaxLucro", LpMaximize)

problema += 3000 * milho + 3500 * soja + 2500 * trigo, "objetivo"

# Limite de Recursos
problema += milho + soja + trigo <= 150 # Área
problema += 2000 * milho + 1700 * soja + 1500 * trigo <= 280000 # Água
problema += 50 * milho + 70 * soja + 40 * trigo <= 7500 # Fertilizante
problema += 4 * milho + 3 * soja + 2 * trigo <= 500 # Pesticida

# Rotação e Alocação de Cultivos
problema += trigo >= 0.3 * (milho + soja + trigo) # Trigo
problema += (milho + soja) >= 0.7 * (milho + soja + trigo) # Milho e Soja

problema.solve(GLPK_CMD())

print('Valor ótimo: ' + str(value(problema.objective)))
print('Solução ótima: ')
for variavel in problema.variables():
    print(' ' + variavel.name + " = " + str(variavel.varValue))