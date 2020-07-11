# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:27:58 2020

@author: felip
"""


class Resultado_Ejecucion:
    def __init__(self):
        self.__id = ""
        self.__id_ejecucion = ""
        self.__fitness = ""
        self.__inicio = ""
        self.__fin = ""
        self.__mejor_solucion = ""
        
        
    def setId(self,ID):
        self.__id = ID
        
    def setIdEjecucion(self,IDE):
        self.__id_ejecucion = IDE
        
    def setFitness(self,fitness):
        self.__fitness = fitness
        
    def setInicio(self,inicio):
        self.__inicio = inicio
        
    def setFin(self,fin):
        self.__fin = fin
        
    def setMejorSolucion(self,MS):
        self.__mejor_solucion = MS
        
    def getId(self):
        return self.__id
    
    def getIdEjecucion(self):
        return self.__id_ejecucion
    
    def getFitness(self):
        return self.__fitness
    
    def getInicio(self):
        return self.__inicio
    
    def getFin(self):
        return self.__fin
    
    def getMejorSolucion(self):
        return self.__mejor_solucion