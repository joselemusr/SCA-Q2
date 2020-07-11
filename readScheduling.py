__author__ = 'INVESTIGACION'
import numpy as np
def importaMatrix(fo,cont):
    i = 0
    k = 0
    columna = 0
    for line in fo.readlines():
        line = line.replace(' ',';').replace('\n','')
        linea = line.split(';')
        estado = 1
        while estado > 0:
            if '' in linea:
                linea.remove('')
                estado = 1
            else:
                estado = 0
        if i == 0:
            print (linea)
            row = int(linea[1])
            col = int(linea[0])
            print (row,col)
            pesos = np.zeros(col)
            matrix = np.zeros((row, col))

        #elif i > 0 and i <85:
        #elif i > 0 and i <668:#AA4
        #elif i > 0 and i <324:
        elif i > 0 and i <cont: #AA3

            for j in range(0,len(linea)):

                pesos[k] = linea[j]
                k = k + 1
            #print 'En la linea', i, k, linea
        else:
                #print 'Segunda etapa',linea
                #print 'Vuelta'
                for h in range(1,len(linea)):
                    matrix[int(linea[h])-1, columna] = 1
                columna = columna + 1
                #print 'La columna', columna
        i = i + 1
    return pesos, matrix

def generaMatrix(file,directory, cont):
    """
        Encargada de leer un archivo donde pasamos el nombre, directorio
    """
    fo = open(directory + file ,'r')
    pesos, matrix = importaMatrix(fo,cont)

    return pesos, matrix
