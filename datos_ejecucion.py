# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:27:44 2020

@author: felip
"""


class Datos_Ejecucion:
    def __init__(self):
        self.__id = ""
        self.__nombre_algoritmo = ""
        self.__parametros = ""
        self.__inicio = ""
        self.__fin = ""
        self.__estado =""
    
    def setID(self,ID):
        self.__id = ID
    
    def setNombreAlgoritmo(self,nombre):
        self.__nombre_algoritmo = nombre
    
    def setParametros(self,parametros):
        self.__parametros = parametros
        
    def setInicio(self,inicio):
        self.__inicio = inicio
        
    def setFin(self,fin):
        self.__fin = fin
        
    def setEstado(self,estado):
        self.__estado = estado
        
    def getId(self):
        return self.__id
    
    def getNombreAlgoritmo(self):
        return self.__nombre_algoritmo
    
    def getParametros(self):
        return self.__parametros
    
    def getInicio(self):
        return self.__inicio
    
    def getFin(self):
        return self.__fin
    
    def getEstado(self):
        return self.__estado
    
    