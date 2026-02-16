from pulp import *

Larger = LpVariable("Larger", lowBound=0, cat='Integer')
Ale = LpVariable("Ale", lowBound=0, cat='Integer')
Ipa = LpVariable("Ipa", lowBound=0, cat='Integer')

problema = LpProblem("MaxLucro", LpMaximize)

problema += 5 * Larger + 6 * Ale + 7 * Ipa, "objetivo"

# Limite de Recursos
problema += 0.4 * Larger + 0.5 * Ale + 0.6 * Ipa <= 1500 # Malte
problema += 0.01 * Larger + 0.015 * Ale + 0.02 * Ipa <= 100 # Lúpulo
problema += 1 * Larger + 1.2 * Ale + 1.5 * Ipa <= 4000 # Água

# Demanda Mínima
problema += Larger >= 200
problema += Ale >= 150
problema += Ipa >= 100

problema.solve(GLPK_CMD())

print('Valor ótimo: ' + str(value(problema.objective)))
print('Solução ótima: ')
for variavel in problema.variables():
    print(' ' + variavel.name + " = " + str(variavel.varValue))