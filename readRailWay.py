__author__ = 'INVESTIGACION'
import numpy as np
def importaMatrix(file, directory):
    fo = open(directory + file,'r')
    i = 0
    for line in fo.readlines():
        linea = line.split(' ')
        linea.remove('')
        linea.remove('\n')
        if i == 0:
            row = int(linea[0])
            col = int(linea[1])
            pesos = np.zeros(col)
            matrix = np.zeros((row, col))
            #print linea

        else:
            linea = line.split(' ')
            linea.remove('')
            linea.remove('\n')
            #print linea
            pesos[i-1] = int(linea[0])
            for j in range(2, int(linea[1])+2):

                matrix[(int(linea[j])-1,i-1)] = 1
                if i == 1:
                    print (int(linea[j]))
        i = i + 1


    return pesos, matrix

