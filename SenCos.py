__author__ = 'INVESTIGACION'
from numpy import zeros
from scipy.special import *
from copy import  deepcopy
import numpy as np
import setCovering as sC
import kmeans as km
import V1 as v1
import V2 as v2
import V3 as v3
import V4 as v4
import S1 as s1
import S2 as s2
import S3 as s3
import S4 as s4
import trasition as tr
import solution as sl
import random as rn
import timeUtility as tU
import math



def completaVector(vector,p):
    vector = sorted(vector)
    nvector = zeros(len(p))
    nxt = vector[0]
    puntero = 0
    for i in range(0,len(p)):
        if nxt == i:
            if puntero < len(vector)-1:
                puntero = puntero + 1
                nxt=vector[puntero]
                nvector[i] = 1
    return nvector

def deltaBH(lsolucion, best,p,Itermax,i):
    #b = 3/2
    #sigma = (gamma(1+b)*np.sin(np.pi *b/2)/(gamma((1+b)/2)*b*2**((b-1)/2)))**(1/b)
    s = deepcopy(lsolucion)
    #u = np.random.randn(len(p))*sigma # Un vector aleatorio de dimension de s, con valores entre [0,1]
    #v = np.random.randn(len(p)) # Otro vector aleatorio
    #step = u/(abs(v)**(1/b))
    step = np.random.uniform(low=0.0, high=1.0)
    scom = completaVector(s,p)
    bestcomp =completaVector(best,p)
    stepsize = np.zeros(len(scom))
    #stepsize=0.01*step*(scom - bestcomp) # Revisar las multimplicaciones de vectores
    a = 2
    r1 = a-i*(a/Itermax)
    for i in range(len(scom)):
        r2 = (2*math.pi)*np.random.uniform(low=0.0, high=1.0)
        r3 = 2*np.random.uniform(low=0.0, high=1.0)
        r4 = np.random.uniform(low=0.0, high=1.0)
        if r4 < 0.5:
            stepsize[i] = scom[i]+(r1*math.sin(r2))*math.fabs((r3*bestcomp[i] - scom[i]))
        else:
            stepsize[i] = scom[i]+(r1*math.cos(r2))*math.fabs((r3*bestcomp[i] - scom[i]))
    return stepsize

def obtieneDelta(llistaSoluciones, best,p,iteracion,Itermax,i):
    delta = zeros(len(p)*len(llistaSoluciones))
    contador = 0
    estado = 0
    for i in range(0,len(llistaSoluciones)):
        dlt = deltaBH(llistaSoluciones[i], best,p,Itermax,i)

        ################################################################################################################
        # Inicio escritura de valores iniciales
        ################################################################################################################
        #import jsonUtil as js

        #estado = js.generaDctInicial(iteracion,i,dlt, estado)
        ################################################################################################################
        # Fin escritura de valores iniciales
        ################################################################################################################


        for j in range(0,len(dlt)):
            delta[contador] = abs(dlt[j])
            #print 'La iteracion', (i+1)*j, (i+1),j, contador
            contador = contador + 1
    return delta

def cuentaGrupos(lgrupos, nGrupos):
    resultCount = []
    for i in range(0,nGrupos):
        resultCount.append(len([elem for elem in lgrupos if elem == i]))
    return resultCount

def filtra(ldelta):

    return len([elem for elem in ldelta if elem >0]), len(ldelta)

def iterar(llistaSoluciones,best,p,matrix,rHeuristic,dictcHeuristics,dict,cHeuristic, iteracion,dictCol,Itermax,i,accion):
    #Obtiene el mejor
    parametroDistancia = 3
    listaSoluciones = []
    timeI = tU.obtieneTime()
    best = sC.recoveryBest(llistaSoluciones,p,best)
    lDelta = obtieneDelta(llistaSoluciones,best,p,iteracion,Itermax,i)
    ###Binarización###
    #print(rand)
    """
    if binarizacion_elegida == 0:
        #------------------------------------------------------------------------------------------------------------------
        ###Kmeans
        #------------------------------------------------------------------------------------------------------------------
        lgrupos, lcentroides = km.obtieneGrupos(lDelta)
        resultCount = cuentaGrupos(lgrupos,len(lcentroides))
        lprobabilidades = km.obtieneProbabilidades(lgrupos,lcentroides)
        #------------------------------------------------------------------------------------------------------------------
    """
    binarizacion_elegida = accion
    ###Funciones de Transferencia
    #------------------------------------------------------------------------------------------------------------------
    if binarizacion_elegida == 0:
        ###V-Shaped_1
        lprobabilidades = v1.obtieneProbabilidades(lDelta)
    if binarizacion_elegida == 1:
        ###V-Shaped_2
        lprobabilidades = v2.obtieneProbabilidades(lDelta)
    if binarizacion_elegida == 2:
        ###V-Shaped_3
        lprobabilidades = v3.obtieneProbabilidades(lDelta)
    if binarizacion_elegida == 3:
        ###V-Shaped_4
        lprobabilidades = v4.obtieneProbabilidades(lDelta)
    if binarizacion_elegida == 4:
        ###S-Shaped_1
        lprobabilidades = s1.obtieneProbabilidades(lDelta)
    if binarizacion_elegida == 5:
        ###S-Shaped_2
        lprobabilidades = s2.obtieneProbabilidades(lDelta)
    if binarizacion_elegida == 6:
        ###S-Shaped_3
        lprobabilidades = s3.obtieneProbabilidades(lDelta)
    if binarizacion_elegida == 7:
        ###S-Shaped_4
        lprobabilidades = s4.obtieneProbabilidades(lDelta)
    #------------------------------------------------------------------------------------------------------------------

    estadoIni = 0
    estadoFin = 0
    row, cols = matrix.shape
    for i in range(0,len(llistaSoluciones)):
        if sC.obtieneDistancia(best,llistaSoluciones[i]) < parametroDistancia: #Si la cantidad de dimensiones distintas es menos a "parametroDistancia" entonces se genera una nueva solución
            lSolution = []
            #lSolution.append(rn.randint(0,500))
            lSolution.append(rn.randint(0,cols)-1)
            lSolution = sl.generaSolucion(lSolution,matrix,p,rHeuristic,dictcHeuristics,dict,cHeuristic,dictCol)
            listaSoluciones.append(sC.mejoraSolucion(lSolution,matrix))
        else:
            elementoIterado = tr.iterarElemento(llistaSoluciones[i],best,lprobabilidades[i*len(p):(i+1)*len(p)])
            ######################################################################################################
            #Para capturar las velocidades intermedias
            #estadoIni = js.getDctInterFin(iteracion,i,llistaSoluciones[i], elementoIterado,estadoIni , 'VelocidadesInter.csv')
            ######################################################################################################

            lSolution = sl.generaSolucion(elementoIterado,matrix,p,rHeuristic,dictcHeuristics,dict,cHeuristic,dictCol)
            ######################################################################################################
            #Para capturar las velocidades intermedias
            #estadoFin = js.getDctInterFin(iteracion,i,llistaSoluciones[i], lSolution,estadoFin , 'VelocidadesFinal.csv')
            ######################################################################################################
            listaSoluciones.append(sC.mejoraSolucion(lSolution,matrix))
    timeF = tU.obtieneTime()
    #print timeI, timeF, 'Heuristica'
        #elementoReparado = rp.generaEliminaciones(p,c,b,elementoIterado)
        #llistaSoluciones[i] = rp.generarInserciones(p,c,b,elementoReparado,dct)
    return listaSoluciones