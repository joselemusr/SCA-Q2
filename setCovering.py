__author__ = 'INVESTIGACION'

import numpy as np
from copy import deepcopy

def fitnessFunction(lSolucion, pesos):
    valorFitness = 0
    for i in range(0,len(lSolucion)):
        valorFitness = valorFitness + pesos[lSolucion[i]]
    return valorFitness

def repeticionSolucion(lSolucion,matrix):
    row, col = matrix.shape
    W = np.zeros(row)
    for j in range(0,len(lSolucion)):
        W = W + matrix[:,lSolucion[j]]
    return W.min(), W

def mejoraSolucion(S,matrix):
    codigoValidez, W = repeticionSolucion(S,matrix)
    S.sort(reverse=True)
    Sf = deepcopy(S)
    for j in range(0, len(S)):
        A = np.where(matrix[:,S[j]]==1)
        B = np.where(W > 1)
        C = np.intersect1d(A[0],B[0])
        if len(A[0]) == len(C):
            #print 'se puede eliminar'
            Sf.remove(S[j])
            codigoValidez, W = repeticionSolucion(Sf,matrix)
    return Sf

def recoveryBest(listalSolucion,pesos, best):
    #print best
    pBest = fitnessFunction(best,pesos)
    for i in range(0,len(listalSolucion)):
        if fitnessFunction(listalSolucion[i],pesos) < pBest:
            best = deepcopy(listalSolucion[i])
            pBest = fitnessFunction(listalSolucion[i],pesos)
    return best

def obtieneDistancia(elem1, elem2):
    c = set(elem1).union(set(elem2))
    d = set(elem1).intersection(set(elem2))
    return len(list(c - d))
