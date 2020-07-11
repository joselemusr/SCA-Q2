__author__ = 'INVESTIGACION'

import random
from copy import deepcopy
import solution as sl


def perturbaSolucion(best,fuerzaPerturbacion):
    # SOlo iniciamos con la solucion
    bestt = deepcopy(best)
    for i in range(0,fuerzaPerturbacion):

        bestt.remove(bestt[random.randint(0, len(bestt)-1)])

    return bestt

def generaPerturbacion(matrix,rHeuristic,dictcHeuristics,pesos, best, fuerzaPerturbacion, dict,cHeuristic,dictCol):
    bestT = deepcopy(perturbaSolucion(best,fuerzaPerturbacion))
    ##############################################################################################################################
    # Lo agregamos para que salga del local
    bestT.append(obtenerAleatorio(bestT,pesos))
    ##############################################################################################################################
    bestT = sl.generaSolucion(bestT,matrix,pesos,rHeuristic,dictcHeuristics,dict,cHeuristic,dictCol)
    #BH = reparaSolucion(p,c,b,BH,dct)
    return bestT

def generaListaPerturbacion(matrix,rHeuristic,dictcHeuristics,pesos,llistasoluciones,fuerzaPerturbacion,dict,cHeuristic,dictCol):
    for i in range(0,len(llistasoluciones)):
        llistasoluciones[i] = generaPerturbacion(matrix,rHeuristic,dictcHeuristics,pesos,llistasoluciones[i],fuerzaPerturbacion,dict,cHeuristic,dictCol)
    return llistasoluciones


def obtenerAleatorio(best,p):
        X = range(0,len(p))
        aleatorios = list(set(X) - set(best))
        return aleatorios[random.randint(0, len(aleatorios)-1)]