# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:28:08 2020

@author: felip
"""


class Datos_Iteracion:
    def __init__(self):
        self.__id = ""
        self.__id_ejecucion = ""
        self.__numero_iteracion = ""
        self.__fitness_mejor = ""
        self.__fitness_promedio = ""
        self.__fitness_mejor_iteracion = ""
        self.__parametros_iteracion = ""
        self.__inicio = ""
        self.__fin = ""
        self.__datos_internos = ""
        
        
    def setId(self,ID):
        self.__id = ID
        
    def setIdEjecucion(self,IDE):
        self.__id_ejecucion = IDE
        
    def setNumeroItearcion(self,NI):
        self.__numero_iteracion = NI
        
    def setFitnessMejor(self,FM):
        self.__fitness_mejor = FM
        
    def setFitnessPromedio(self,FP):
        self.__fitness_promedio = FP
        
    def setFitnessMejorIteracion(self,FMI):
        self.__fitness_mejor_iteracion = FMI
        
    def setParametrosIteracion(self,PI):
        self.__parametros_iteracion = PI
        
    def setInicio(self,inicio):
        self.__inicio = inicio
    
    def setFin(self,fin):
        self.__fin = fin
        
    def setDatosInternos(self,DI):
        self.__datos_internos = DI
        
    def getId(self):
        return self.__id
    
    def getIdEjecucion(self):
        return self.__id_ejecucion
    
    def getNumeroIteracion(self):
        return self.__numero_iteracion
    
    def getFitnessMejor(self):
        return self.__fitness_mejor
    
    def getFitnessPromedio(self):
        return self.__fitness_promedio
    
    def getFitnessMejorIteracion(self):
        return self.__fitness_mejor_iteracion
    
    def getParametrosIteracion(self):
        return self.__parametros_iteracion
    
    def getInicio(self):
        return self.__inicio
    
    def getFin(self):
        return self.__fin
    
    def getDatosInternos(self):
        return self.__datos_internos