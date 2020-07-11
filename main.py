__author__ = 'INVESTIGACION'

import sys 
import os 
sys.path.append(os.path.abspath("C:/Personal/Articulos/KNN-Greedy/KMRT-SetCovering-4"))

import Q_Learning as QL
import solution as sl
import random as rn
import readRailWay as rRW
import readOrProblems as rOP
import readScheduling as rS
import heuristic as he
import setCovering as sC
import SenCos as scos
import Q_Learning as QL
from copy import deepcopy
import perturbation as pt
import timeUtility as tU
from random import choice

import sqlalchemy as db
from sqlalchemy import text
import json
import pickle 
import zlib
import psycopg2
#import datetime
from datetime import datetime
#import MySQLdb

import datos_ejecucion as DE
import datos_iteracion as DI
import resultado_ejecucion as RE




#f= ['scp41.txt','scp42.txt','scp43.txt','scp44.txt','scp45.txt']
#f = [sys.argv[1]] #instancia
#desde = int(sys.argv[2])
#hasta = int(sys.argv[3])
#poblacion = int(sys.argv[4]) 
#iteraciones = int(sys.argv[5])
#alpha = int(sys.argv[6]) #ALPHA ESTATICO = 1, ALPHA ITERACIONES = 2, ALPHA VISITAS = 3
#recompensa = int(sys.argv[7])  #+1-1 = 1, +1-0 = 2


#carpeta = './Problemas/'
#carpetarpetaResultados = 'resultados/scp'

#El host se actualiza cada vez que se prenda la maquina donde esta la BD
host = "35.188.84.116" 
port = "5432"
user = "mh"
pwd = "mh"
db_name = "resultados_mh"
engine = db.create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{db_name}', connect_args={'connect_timeout': 1000})
metadata = db.MetaData()
connection = engine.connect()


datosEjecucion = db.Table('datos_ejecucion', metadata, autoload=True, autoload_with=engine)
resultadoEjecucion = db.Table('resultado_ejecucion', metadata, autoload=True, autoload_with=engine)
insertDatosEjecucion = datosEjecucion.insert().returning(datosEjecucion.c.id)
datosIteracion = db.Table('datos_iteracion', metadata, autoload=True, autoload_with=engine)
insertDatosIteracion = datosIteracion.insert()

insertResultadoEjecucion =resultadoEjecucion.insert()
sql = text("""update datos_ejecucion set estado = 'ejecucion', inicio = :inicio
                where id = 
                (select id from datos_ejecucion
                    where estado = 'pendiente' and Nombre_Algoritmo = 'SCA-Q2'
                    order by id asc
                    limit 1) returning id, parametros;""")



dirIn = './Problemas/'

#OPTIMO = []

##PArametrizar
#OPTIMO.append(optimo6[0])


while True:
    inicio_Total = datetime.now()
    arrResult = connection.execute(sql,**{"inicio":inicio_Total}).fetchone()
    if arrResult is None: 
        break
    idEjecucion = arrResult[0]
    param = json.loads(arrResult[1])

    try :
        f = param['instancia']
        print(f'file = {f}')
        OPTIMO = int(param['MinInstancia'])
        poblacion = param['poblacion']
        iteraciones = param['iteraciones']
        alpha = int(param['alpha']) #ALPHA ESTATICO = 1, ALPHA ITERACIONES = 2, ALPHA VISITAS = 3
        recompensa = int(param['recompensa']) #+1-1 = 1, +1-0 = 2
        

        #fileOut = file[:len(file) -4] + 'Salida.txt' #Define nombre del archivo de salida
        pesos, matrix = rOP.generaMatrix(f,dirIn) #Se generan los pesos y la matrix desde la instancia a ejecutar
        row, cols = matrix.shape #Se extrae el tamaño del problema

        #Inicializamos la heuristica
        #print ('iniciando1')
        cHeuristic = []
        #cHeuristic =  he.getHeuristic(matrix,pesos)
        #print ('iniciando2')
        rHeuristic = he.getRowHeuristics(matrix)
        #print ('iniciando3')
        dict = he.getRowColumn(matrix)
        dictCol = he.getColumnRow(matrix)
        #print ('iniciando4')
        #dictcHeuristics = he.getColumnsDict(cHeuristic)0
        dictcHeuristics = {}
        listalSolucion = []
        #print ('iniciando5')


        #Generar Población inicial
        listalSolucion = [] #Lista con todas las soluciones
        #Registro = open("Resultados/" + str("SenCos_Hyper_QL") + "_" + str(file) + "_" + str(j) + ".txt", "w") 
        Poblacion = int(poblacion)
        for z in range(0,Poblacion): #por cada individuo 
            lSolution = [] 

            for i in range(rn.randint(0,cols)-1):  #Elijo una cantidad de columas a poner en 1
                lSolution.append(rn.randint(0,cols)-1) #Elijo la columna a poner en 1
            lSolution = list(set(lSolution)) #Elimino los repetidos si es que tiene

            lSolution = sl.generaSolucion(lSolution,matrix,pesos,rHeuristic,dictcHeuristics,dict,cHeuristic,dictCol)
            listalSolucion.append(lSolution)  
            #print("Individuo " + str(z) + ": " + str(sC.fitnessFunction(lSolution,pesos)))
            #Registro.write("Individuo :" + str(z+1) +" ,")
            #Registro.write(str(sC.fitnessFunction(lSolution,pesos)) + ",")
            #timeIni = tU.obtieneTime() #Registro del tiempo 
            #Registro.write(str(timeIni) + ",\n")            
        #print (listalSolucion)
           
        #BUSCO FITNESS MAS BAJO PARA OBTENER BEST INICIAL
        best = []
        BestFitnessGlobal = None
        
        for o in range(0,Poblacion):
            if BestFitnessGlobal is None or sC.fitnessFunction(listalSolucion[o], pesos) < BestFitnessGlobal:
                best = deepcopy(listalSolucion[o])
                BestFitnessGlobal = sC.fitnessFunction(listalSolucion[o], pesos)
        
        
        #Revisar que pasa acá***
        final = deepcopy(best)
        BestFitnessIter = BestFitnessGlobal
        #Inicial = deepcopy(best)
        #print(f'best = {best}')
        #print(f'pesos = {pesos}')
        #for s in range(len(pesos)):
            #print(f'pesos = {s}, {pesos[s]}')
        #print(f'BestFitnessGlobal= {BestFitnessGlobal}')
        

        #INICIALIZACION Q-LEARNING
        cantidad_acciones = 8 # LAS ACCIONES EN ESTE CASO ES LA BINARIZACION
        Q_Values = QL.iniciar_Q_Values(cantidad_acciones)
        

        visitas = QL.iniciar_visitas(cantidad_acciones)
        
        #Generar iteraciones
        timeIni = tU.obtieneTime() #Registro del tiempo
        Itermax= int(iteraciones)
        #print(f'Itermax = {Itermax}')
        data_iter = []
        

        for i in range(0,Itermax): #For para cada iteración ***El parametro población se debe mover a una lista de constantes
            inicio_iter = datetime.now()

            #SELECCION DE BINARIZACION
            accion = QL.seleccionar_Accion(Q_Values)

            #Ejecución del Algoritmo
            listalSolucion = scos.iterar(listalSolucion,best,pesos,matrix,rHeuristic,dictcHeuristics,dict,cHeuristic,i,dictCol,Itermax,i,accion[1])  #realiza la iteracion sobre la lista

            #BUSCO EL MEJOR BEST OBTENIDO EN LA ITERACION
            
            
            for o in range(0,Poblacion):
                if sC.fitnessFunction(listalSolucion[o], pesos) < BestFitnessGlobal:
                    best = deepcopy(listalSolucion[o])
                    BestFitnessGlobal = sC.fitnessFunction(listalSolucion[o], pesos)

            #Calculo del nuevo Q_Learning
            Q_nuevo = QL.Q_Nuevo_Minimizacion(Q_Values,visitas,accion,BestFitnessGlobal,BestFitnessIter,i,Itermax,alpha,recompensa)
            
            if alpha == 3:
                visitas = QL.actualizar_Visitas(visitas,accion)
            
            Q_Values = QL.actualizar_Q_Values(Q_Values,accion,Q_nuevo)
            
            #BestFitnessGlobal = sC.fitnessFunction(best,pesos)
            #print(f'best = {best}')
            #print(f'pesos = {pesos}')
            #print(f'BestFitnessGlobal= {BestFitnessGlobal}')
            #BestFitnessIter = sC.fitnessFunction(final,pesos)

            if BestFitnessGlobal < BestFitnessIter: # mejora la solucion 
                final = deepcopy(best)
                BestFitnessIter = sC.fitnessFunction(final,pesos)
            #Comenté este If, porque quiero guardar la acción para todas las iteraciones
            fin_iter = datetime.now()
            datosInternos = {
                'Fitness' : BestFitnessGlobal,
                }
            datosInternos = zlib.compress(pickle.dumps(datosInternos))

            data_iter.append({
                'id_ejecucion' : idEjecucion
                ,'fitness_mejor' : BestFitnessGlobal
                ,'fitness_Iter' : BestFitnessIter
                ,'iter': i
                ,'accion': accion[1]
                ,'inicio' : inicio_iter
                ,'fin' : fin_iter
                #,'parametros_iteracion' : json.dumps({'nivel': nivel})
                ,'datos_internos' : datosInternos}
                )

            #REGISTRO ITERACION -> BEST FITNESS, BEST FITNESS ITERACION, FIN, PARAMETRO (BINARIZACION)
            #ite.setFitnessMejor(BestFitnessIter)
            #ite.setFitnessMejorIteracion(BestFitnessGlobal)
            #ite.setParametrosIteracion(accion[1])
            
            #iteracion.append(ite)
            #print(f'OPTIMO = {OPTIMO}')
            #print(f'Fitness = {BestFitnessGlobal}')
            if sC.fitnessFunction(best, pesos) <= OPTIMO and OPTIMO != 0.0:
            #if BestFitnessGlobal <= OPTIMO and OPTIMO != 0.0:
                fin_iter = datetime.now()
                #print(f'OPTIMO Salio! = {OPTIMO}')

                datosInternos = {
                    'Fitness' : BestFitnessGlobal,
                    }
                datosInternos = zlib.compress(pickle.dumps(datosInternos))

                data_iter.append({
                    'id_ejecucion' : idEjecucion
                    ,'fitness_mejor' : BestFitnessGlobal
                    ,'fitness_Iter' : BestFitnessIter
                    ,'iter': i
                    ,'accion': accion[1]
                    ,'inicio' : inicio_iter
                    ,'fin' : fin_iter
                    #,'parametros_iteracion' : json.dumps({'nivel': nivel})
                    ,'datos_internos' : datosInternos}
                    )
                break

        fin_Total = datetime.now()
        #print(f'Fitness Salio2! = {sC.fitnessFunction(best, pesos)}')
        updateDatosEjecucion = datosEjecucion.update().where(datosEjecucion.c.id == idEjecucion)
        connection.execute(updateDatosEjecucion, {'fin':fin_Total, 'estado' : 'terminado'})
        connection.execute(insertResultadoEjecucion, {
            'id_ejecucion':idEjecucion
            ,'numero_iteracion' : Itermax
            ,'fitness' : BestFitnessGlobal
            ,'inicio': inicio_Total 
            ,'fin': fin_Total
            })

        connection.execute(insertDatosIteracion, data_iter)
    


    except Exception as error:   
        updateDatosEjecucion = datosEjecucion.update().where(datosEjecucion.c.id == idEjecucion)
        connection.execute(updateDatosEjecucion, {'inicio':None,'fin':None, 'estado' : 'pendiente'})
        raise error 