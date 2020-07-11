# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 17:03:54 2020

@author: Felipe Cisternas
"""

import numpy as np
from copy import deepcopy
import random


q0 = 0.9
ro = 0.4
E = 0.05


def iniciar_Q_Values(cantidad): # CANTIDAD CORRESPONDE A LA CANTIDAD DE ACCIONES A UTILIZAR 
                                # EN ESTE CASO SON 8 (S1,S2,S3,S4,V1,V2,V3,V4) TODAS CON DISCRETIZACION ELITISTA
    Q_Values = []
    for i in range(0,cantidad):
        Q_Values.append(q0)
    return Q_Values


def iniciar_visitas(cantidad): # CORRESPONDE A UN PARAMETRO DE "SIGNIFICACIA" PARA CADA UNA DE LAS ACCIONES
                                # MIENTRAS  MAS SE VISITEN MAYOR ES SU SIGNIFICANCIA (FACTOR DE APRENDIZAJE)
    visitas = []
    for i in range(0,cantidad):
        visitas.append(0)
    return visitas

def seleccionar_Accion(Q_Values): # SELECCION DE ACCION
    Q_posicion =[]
    Q_mayores = []
    accion = []
    mayor = -1412412
    
    p = np.random.uniform(low=0.0, high=1.0) # VALOR ALEATORIO ENTRE [0,1]
    
    if p <= E: # SI ES MEJOR O IGUAL A 0.05
        for i in range(0,Q_Values.__len__()): #SELECCION ALEATORIA
            Q_posicion.append(i)
        posicion = random.choice(Q_posicion)
        accion.append(Q_Values[posicion])
        accion.append(posicion)
    else: #SELECCION DE LA ACCION CON Q-VALUE MAS ALTO
        for i in range(0,Q_Values.__len__()):
            if Q_Values[i] > mayor:
                mayor = Q_Values[i]
        
        for i in range(0,Q_Values.__len__()):
            if Q_Values[i] == mayor:
                Q_mayores.append(Q_Values[i])
                Q_posicion.append(i)
        elegido = random.choice(Q_posicion)
        posicion = 0
        for i in range(0,Q_posicion.__len__()):
            if Q_posicion[i] == elegido:
                posicion = i
    
        accion.append(Q_mayores[posicion])
        accion.append(Q_posicion[posicion])
    return accion

def Q_Nuevo_Minimizacion(Q_Values,visitas,accion,best,resultado,i,Itermax,alp,recompensa): #ACTUALIZACION DE Q-VALUE
    
    
        
    q_max = obtener_Q_MAX(Q_Values)
    
    #alpha estatico 
    if alp == 1:
        alpha = 0.1
    
    #alpha dinamico, iteraciones
    if alp == 2:
        alpha = 1 - (0.9*(i/Itermax))
    
    #alpha dinamico, visitas
    if alp == 3:
        alpha = (1/(1 + visitas[accion[1]]))
    
    
    r = recompensar(best,resultado,recompensa)

    Q_nuevo = ( (1-alpha) * Q_Values[accion[1]] ) + ( alpha * ( r + ( ro * q_max) ) )
    
    return Q_nuevo

def recompensar(best,resultado,recompensa):
    
    if recompensa == 1:
        if best < resultado: #mejoro la solucion
            return  1
        else:
            return -1
        
    if recompensa == 2:
        if best < resultado: #mejoro la solucion
            return  1
        else:
            return 0
    


def obtener_Q_MAX(Q_Values):
    return max(Q_Values)    
    """
    segundo_mayor = 0
    
    for i in range(0,Q_Values.__len__()):
        evaluar = Q_Values[i]
        flag = 0
        for j in range(0,Q_Values.__len__()):
            if evaluar < Q_Values[j] and Q_Values[j] != mayor:
                flag = 1
        if flag == 0 and evaluar != mayor:
            segundo_mayor = evaluar 
                
    return segundo_mayor
    """

def actualizar_Q_Values(Q_Values,accion,Q_nuevo): #ACTUALIZACION DE Q-VALUE
    Q_Values[accion[1]] = Q_nuevo
    return Q_Values

def actualizar_Visitas(visitas,accion): # ACTUALIZACION DE LAS VISITAS
    visitas[accion[1]] = visitas[accion[1]] + 1
    return visitas
    
    

     
    
