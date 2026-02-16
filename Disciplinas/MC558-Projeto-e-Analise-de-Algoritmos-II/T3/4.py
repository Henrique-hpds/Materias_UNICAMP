from pulp import *

Analgesico = LpVariable("Analgesico", lowBound=0, cat='Integer')
Antibiotico = LpVariable("Antibiotico", lowBound=0, cat='Integer')
Antialergico = LpVariable("Antialergico", lowBound=0, cat='Integer')

problema = LpProblem("MaxLucro", LpMaximize)

problema += 8 * Analgesico + 12 * Antibiotico + 10 * Antialergico, "objetivo"

# Limite de Recursos
problema += 10 * Analgesico + 15 * Antibiotico + 12 * Antialergico <= 3000 # Ingrediente A
problema += 5 * Analgesico + 8 * Antibiotico + 10 * Antialergico <= 2000 # Ingrediente B
problema += 0.5 * Analgesico + 0.8 * Antibiotico + 0.6 * Antialergico <= 150 # Tempo de Máquina

# Demanda Mínima
problema += Analgesico >= 100
problema += Antibiotico >= 50
problema += Antialergico >= 75

problema.solve(GLPK_CMD())

print('Valor ótimo: ' + str(value(problema.objective)))
print('Solução ótima: ')
for variavel in problema.variables():
    print(' ' + variavel.name + " = " + str(variavel.varValue))