
from pulp import *

print('Benvenuti nel programma di soluzione dei problemi di programmazione lineare.\n1. Si prega di scrivere "massimizzare" se si vuole massimizzare la funzione o "minimizzare" se la si vuole minimizzare seguiti dal pulsante INVIO.\n2. Si prega di inserire la funzione da massimizzare/minimizzare e premere INVIO.\n3. Si prega di inserire i vincoli seguiti dal pulsante INVIO.\n4. Terminati ivincoli si prega di scrivere "fine" e premere INVIO.\n\nOperatori:\nSomma: +\nSottrazione: -\nMoltiplicazione: *\nDivisione: /\nMinore uguale: <=\nMaggiore uguale: >=')
for i in range(0, 99999):
    #print(i)
    str = 'x{0} = LpVariable("x{1}", lowBound=0)'.format(i+1,i+1)
    exec(str)

print('')
maxmin = input('Inserire "massimizzare" o "minimizzare": ')

while True:
    if maxmin != "massimizzare" and maxmin != "minimizzare":
        maxmin = input('Impossimile soddisfare la richiesta.\nInserire "massimizzare" o "minimizzare":')
    else:
        break

if maxmin == 'massimizzare':
    problem = LpProblem('Massimizzazione',LpMaximize)
    minmax = 'max'
else:
    problem = LpProblem('Minimizzazione',LpMinimize)
    minmax = 'min'

try:
    funzione = eval(input(f'Inserire la funzione da {maxmin}: {minmax} z = '))
    problem += funzione
except:
    funzione = eval(input(f'Tipologia di dato inserito non corretta.\nInserire la funzione da {maxmin}: {minmax} z = '))
    problem += funzione

while True:
    try:
        vincolo = eval(input('Inserire vincolo: '))
        problem += vincolo
    except NameError:
        break

if maxmin == 'massimizzare':
    illimit = 'superiormente'
else:
    illimit = 'inferiormente'

problem.solve()
stato = LpStatus[problem.status]
if stato == 'Unbounded':
    print(f'Il problema è illimitato {illimit}')
elif stato == 'Infeasible':
    print('Il problema è inammissibile')
else:
    print ("Risultati della ottimizzazione:")
for variabile in problem.variables():
    print (variabile.name, "=", variabile.varValue)
print ("Ottimizzazione totale:")
print (value(problem.objective))
