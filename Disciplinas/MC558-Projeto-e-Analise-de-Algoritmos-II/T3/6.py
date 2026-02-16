from pulp import *

Tinto = LpVariable("Tinto", lowBound=0, cat='Integer')
Branco = LpVariable("Branco", lowBound=0, cat='Integer')
Rose = LpVariable("Rose", lowBound=0, cat='Integer')

problema = LpProblem("MaxLucro", LpMaximize)

problema += 50 * Tinto + 40 * Branco + 45 * Rose, "objetivo"

# Limite de Recursos
problema += 1.2 * Tinto + 0.8 * Branco + 1 * Rose <= 1500 # Uva
problema += 0.1 * Tinto + 0.1 * Branco + 0.1 * Rose <= 70 # Espaço

# Demanda Mínima
problema += Tinto >= 100
problema += Branco >= 80
problema += Rose >= 60

problema.solve(GLPK_CMD())

print('Valor ótimo: ' + str(value(problema.objective)))
print('Solução ótima: ')
for variavel in problema.variables():
    print(' ' + variavel.name + " = " + str(variavel.varValue))