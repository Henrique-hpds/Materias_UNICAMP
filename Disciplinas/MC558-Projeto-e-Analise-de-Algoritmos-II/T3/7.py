from pulp import *

Chocolate = LpVariable("Chocolate", lowBound=0, cat='Integer')
Baunilha = LpVariable("Baunilha", lowBound=0, cat='Integer')
Morango = LpVariable("Morango", lowBound=0, cat='Integer')

problema = LpProblem("MaxLucro", LpMaximize)

problema += 12 * Chocolate + 10 * Baunilha + 11 * Morango, "objetivo"

# Limite de Recursos
problema += 0.5 * Chocolate + 0.4 * Baunilha + 0.45 * Morango <= 500 # Leite
problema += 0.1 * Chocolate + 0.15 * Baunilha + 0.12 * Morango <= 80 # Açúcar
problema += 10 * Chocolate + 8 * Baunilha + 9 * Morango <= 2000 # Saborizantes

# Demanda Mínima
problema += Chocolate >= 80
problema += Baunilha >= 60
problema += Morango >= 50

problema.solve(GLPK_CMD())

print('Valor ótimo: ' + str(value(problema.objective)))
print('Solução ótima: ')
for variavel in problema.variables():
    print(' ' + variavel.name + " = " + str(variavel.varValue))