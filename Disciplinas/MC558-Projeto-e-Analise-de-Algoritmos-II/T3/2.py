from pulp import *

Acido = LpVariable("Acido", lowBound=0, cat='Integer')
Amonia = LpVariable("Amonia", lowBound=0, cat='Integer')
Metanol = LpVariable("Metanol", lowBound=0, cat='Integer')

problema = LpProblem("MaxLucro", LpMaximize)

problema += 50 * Acido + 40 * Amonia + 60 * Metanol, "objetivo"

# Disponibilidade de Recursos
problema += 2 * Acido + 1 * Amonia + 3 * Metanol <= 200
problema += 3 * Acido + 2 * Amonia + 2 * Metanol <= 300
problema += 1 * Acido + 3 * Amonia + 2 * Metanol <= 150

# Poluição
problema += 3 * Acido + 2 * Amonia + 4 * Metanol <= 500

# Horas de Trabalho
problema += 5 * Acido + 3 * Amonia + 6 * Metanol <= 400

problema.solve(GLPK_CMD())

print('Valor ótimo: ' + str(value(problema.objective)))
print('Solução ótima: ')
for variavel in problema.variables():
    print(' ' + variavel.name + " = " + str(variavel.varValue))