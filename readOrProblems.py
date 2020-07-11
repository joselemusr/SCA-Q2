__author__ = 'INVESTIGACION'

import numpy as np

def importaMatrix2(fo, paramLectura):
    i = 0
    fila = 0
    estado = 0
    suma = 0
    for line in fo.readlines():
        linea = line.split(' ')
        linea.remove('')
        if "\n" in linea:
            linea.remove('\n')
        if i == 0:
            row = int(linea[0])
            col = int(linea[1])
            pesos = np.zeros(col)
            matrix = np.zeros((row, col))

        #elif i > 0 and i <85:
        #elif i > 0 and i <668:
        elif i > 0 and i <paramLectura:

            k = 0
            for j in range(0,len(linea)):
                #print(f'j = {j}, k = {k}, Lineas = {len(linea)}, lineaj = {linea[j]}, Pesos[k] = {pesos[k]}')
                pesos[k] = linea[j]
                #print(f'pesos = {pesos}')
                k = k + 1
        else:
            if estado == 0:
                cuenta = int(linea[0])
                estado = 1
            else:
                suma = suma + len(linea)

                for h in range(0,len(linea)):
                    matrix[fila,int(linea[h])-1] = 1
                if suma == cuenta:
                    estado = 0
                    suma = 0
                    fila = fila + 1

        i = i + 1
    return pesos, matrix

def importaMatrix(fo, paramLectura):
    i = 0
    k = 0
    fila = 0
    estado = 0
    suma = 0
    for line in fo.readlines():
        linea = line.split(' ')
        linea.remove('')
        if "\n" in linea:
            linea.remove('\n')
        if i == 0:
            row = int(linea[0])
            col = int(linea[1])
            pesos = np.zeros(col)
            matrix = np.zeros((row, col))

        #elif i > 0 and i <85:
        #elif i > 0 and i <668:
        elif i > 0 and i <paramLectura:

            for j in range(0,len(linea)):
                #print(f'j = {j}, k = {k}, Lineas = {len(linea)}, lineaj = {linea[j]}, Pesos[k] = {pesos[k]}')
                pesos[k] = linea[j]
                #print(f'j = {j}, k = {k}, Lineas = {len(linea)}, lineaj = {linea[j]}, Pesos[k] = {pesos[k]}')
                k = k + 1
        else:
            if estado == 0:
                cuenta = int(linea[0])
                estado = 1
            else:
                suma = suma + len(linea)

                for h in range(0,len(linea)):
                    matrix[fila,int(linea[h])-1] = 1
                if suma == cuenta:
                    estado = 0
                    suma = 0
                    fila = fila + 1

        i = i + 1
    return pesos, matrix

def importaMatrixRed(fo, paramLectura):
    i = 0
    k = 0
    fila = 0
    estado = 0
    suma = 0
    for line in fo.readlines():
        #linea = line.replace('\n','').split(' ')
        #linea.remove('')
        
        linea = line.split(' ')
        vacio = ''
        if vacio in linea:
            linea.remove('')
        if "\n" in linea:
            linea.remove('\n')
        
        if i == 0:
            row = int(linea[0])
            col = int(linea[1])
            pesos = np.zeros(col)
            matrix = np.zeros((row, col))

        #elif i > 0 and i <85:
        #elif i > 0 and i <668:
        elif i > 0 and i <paramLectura:

            for j in range(0,len(linea)):
                #print(f'j1 = {j}, k = {k}, Lineas = {len(linea)}, lineaj = {linea[j]}, Pesos[k] = {pesos[k]}')
                pesos[k] = int(linea[j])
                #print(f'j2 = {j}, k = {k}, Lineas = {len(linea)}, lineaj = {linea[j]}, Pesos[k] = {pesos[k]}')
                k = k + 1
        else:
            if estado == 0:
                cuenta = int(linea[0])
                estado = 1
            else:
                suma = suma + len(linea)

                for h in range(0,len(linea)):
                    #print('linea h',linea[h])
                    matrix[fila,int(linea[h])-1] = 1
                if suma == cuenta:
                    estado = 0
                    suma = 0
                    fila = fila + 1

        i = i + 1
    return pesos, matrix

def LeerInstancia(Archivo):
#        print(f'abriendo archivo {datetime.now()}')
    #Archivo = open(Instancia, "r")
#        print(f'fin abriendo archivo {datetime.now()}')    
    # Leer Dimensión
    Registro = Archivo.readline().split()
    rows = int(Registro[0])
    columns = int(Registro[1])
    
    # Leer Costo
    Costos        = []
    Registro      = Archivo.readline()
    ContVariables = 1
#        print(f'ciclo qlo 1 {datetime.now()}')
    while Registro != "" and ContVariables <= columns :
        Valores = Registro.split()
        for Contador in range(len(Valores)):
            Costos.append(int(Valores[Contador]))
            ContVariables = ContVariables + 1
        Registro = Archivo.readline()
#        print(f'fin ciclo qlo 1 {datetime.now()}')
    # Preparar Matriz de Restricciones.
    
#        print(f'ciclo qlo 2 {datetime.now()}')
    Restricciones = np.zeros((rows, columns))
#        for Fila in range(self.rows):
#            Restricciones.append([])
#            for Columna in range(self.columns):
#                Restricciones[Fila].append(0)
#        print(f'fin ciclo qlo 2 {datetime.now()}')
    # Leer Restricciones    
    ContVariables      = 1
    Fila               = 0
    cont = 0
#        print(f'ciclo qlo 3 {datetime.now()}')
    while Registro != "":
#            if Registro != '\n': 
#            Registro = Registro.strip()
#            Registro = Registro.replace('\n','').replace(" ",',')
#            Registro = np.fromstring(Registro, dtype=int, sep=",")
#            print(np.fromstring(Registro, dtype=int, sep=","))
#            exit()
        CantidadValoresUno = int(Registro)
        ContadorValoresUno = 0
        Registro = Archivo.readline()
#            print(Registro)
        Registro = Registro.replace('\n','').replace("\\n'",'')
#            print(Registro)
        while Registro != "" and ContadorValoresUno < CantidadValoresUno: 
            Columnas = Registro.split() 
            for Contador in range(len(Columnas)):
                Columna = int(Columnas[Contador]) - 1
                Restricciones[Fila][Columna] = 1
                ContadorValoresUno = ContadorValoresUno + 1
            Registro = Archivo.readline()
        Fila = Fila + 1
#        print(f'fin ciclo qlo 3 {datetime.now()}')
    Archivo.close()
    return Costos, Restricciones

def generaMatrix(file,dirIn):
    """
    Encargada de leer un archivo donde pasamos el nombre (file) y el directorio (dirIn)
    """
    
    """
    || INSTANCIA || CANTIDAD ||    MATRIZ    || paramLectura ||
    ===========================================================
    ||    4      ||    10    ||  200 X 1000  ||      85      ||
    ===========================================================
    ||    5      ||    10    ||  200 X 2000  ||     168      ||
    ===========================================================
    ||    6      ||     5    ||  200 X 1000  ||      85      ||
    ===========================================================
    ||    A      ||     5    ||  300 X 3000  ||     201      ||
    ===========================================================
    ||    B      ||     5    ||  300 X 3000  ||     201      ||
    ===========================================================
    ||    C      ||     5    ||  400 X 4000  ||     268      ||
    ===========================================================
    ||    D      ||     5    ||  400 X 4000  ||     268      ||
    ===========================================================
    ||    NRE    ||     5    ||  500 X 5000  ||     335      ||
    ===========================================================
    ||    NRF    ||     5    ||  500 X 5000  ||     335      ||
    ===========================================================
    ||    NRG    ||     5    || 1000 X 10000 ||     668      ||
    ===========================================================
    ||    NRH    ||     5    || 1000 X 10000 ||     668      ||
    ===========================================================
    """

#Instancias NO Reducidas
    ListA = ['scp41.txt','scp42.txt','scp43.txt','scp44.txt','scp45.txt','scp46.txt','scp47.txt','scp48.txt','scp49.txt','scp410.txt','scp61.txt','scp62.txt','scp63.txt','scp64.txt','scp65.txt']
    ListB = ['scp51.txt','scp52.txt','scp53.txt','scp54.txt','scp55.txt','scp56.txt','scp57.txt','scp58.txt','scp59.txt','scp510.txt']
    ListC = ['scpa1.txt','scpa2.txt','scpa3.txt','scpa4.txt','scpa5.txt','scpb1.txt','scpb2.txt','scpb3.txt','scpb4.txt','scpb5.txt']
    ListD = ['scpc1.txt','scpc2.txt','scpc3.txt','scpc4.txt','scpc5.txt','scpd1.txt','scpd2.txt','scpd3.txt','scpd4.txt','scpd5.txt']
    ListE = ['scpnre1.txt','scpnre2.txt','scpnre3.txt','scpnre4.txt','scpnre5.txt','scpnrf1.txt','scpnrf2.txt','scpnrf3.txt','scpnrf4.txt','scpnrf5.txt']
    ListF = ['scpnrg1.txt','scpnrg2.txt','scpnrg3.txt','scpnrg4.txt','scpnrg5.txt','scpnrh1.txt','scpnrh2.txt','scpnrh3.txt','scpnrh4.txt','scpnrh5.txt']
    
    if file in ListA:
        paramLectura = 85

    if file in ListB:
        paramLectura = 168

    if file in ListC:
        paramLectura = 201

    if file in ListD:
        paramLectura = 268

    if file in ListE:
        paramLectura = 335

    if file in ListF:
        paramLectura = 668
        
    if file == 'mscp41.txt':
        paramLectura = 15

#Instancias Reducidas

    List4R = ['mscp41.txt','mscp42.txt','mscp43.txt','mscp44.txt','mscp45.txt','mscp46.txt','mscp47.txt','mscp48.txt','mscp49.txt','mscp410.txt']
    List4RL = [15,19,20,18,19,21,18,19,22,18]
    if file in List4R:
        arg = List4R.index(file)
        paramLectura = List4RL[arg]
    
    List5R = ['mscp51.txt','mscp52.txt','mscp53.txt','mscp54.txt','mscp55.txt','mscp56.txt','mscp57.txt','mscp58.txt','mscp59.txt','mscp510.txt']
    List5RL = [20,23,19,20,17,19,20,22,21,21]
    if file in List5R:
        arg = List5R.index(file)
        paramLectura = List5RL[arg]
    
    List6R = ['mscp61.txt','mscp62.txt','mscp63.txt','mscp64.txt','mscp65.txt']
    List6RL = [19,22,21,18,22]
    if file in List6R:
        arg = List6R.index(file)
        paramLectura = List6RL[arg]
    
    ListAR = ['mscpa1.txt','mscpa2.txt','mscpa3.txt','mscpa4.txt','mscpa5.txt']
    ListARL = [33,34,34,33,34]
    if file in ListAR:
        arg = ListAR.index(file)
        paramLectura = ListARL[arg]
    
    ListBR = ['mscpb1.txt','mscpb2.txt','mscpb3.txt','mscpb4.txt','mscpb5.txt']
    ListBRL = [39,40,43,42,40]
    if file in ListBR:
        arg = ListBR.index(file)
        paramLectura = ListBRL[arg]
    
    ListCR = ['mscpc1.txt','mscpc2.txt','mscpc3.txt','mscpc4.txt','mscpc5.txt']
    ListCRL = [45,48,50,47,47]
    if file in ListCR:
        arg = ListCR.index(file)
        paramLectura = ListCRL[arg]
    
    ListDR = ['mscpd1.txt','mscpd2.txt','mscpd3.txt','mscpd4.txt','mscpd5.txt']
    ListDRL = [55,58,59,56,54]
    if file in ListDR:
        arg = ListDR.index(file)
        paramLectura = ListDRL[arg]
    
    ListER = ['mscpnre1.txt','mscpnre2.txt','mscpnre3.txt','mscpnre4.txt','mscpnre5.txt']
    ListERL = [71,81,75,79,82]
    if file in ListER:
        arg = ListER.index(file)
        paramLectura = ListERL[arg]
    
    ListFR = ['mscpnrf1.txt','mscpnrf2.txt','mscpnrf3.txt','mscpnrf4.txt','mscpnrf5.txt']
    ListFRL = [62,57,64,60,56]
    if file in ListFR:
        arg = ListFR.index(file)
        paramLectura = ListFRL[arg]
    
    ListGR = ['mscpnrg1.txt','mscpnrg2.txt','mscpnrg3.txt','mscpnrg4.txt','mscpnrg5.txt']
    ListGRL = [174,163,168,166,170]
    if file in ListGR:
        arg = ListGR.index(file)
        paramLectura = ListGRL[arg]
    
    ListHR = ['mscpnrh1.txt','mscpnrh2.txt','mscpnrh3.txt','mscpnrh4.txt','mscpnrh5.txt']
    ListHRL = [234,230,232,233,227]
    if file in ListHR:
        arg = ListHR.index(file)
        paramLectura = ListHRL[arg]


    #paramLectura = 85 # Para el caso de los problemas 4, 6
    #paramLectura = 168 # Para el caso de problemas 5
    #paramLectura = 201 # Para el caso de problemas A, B
    #paramLectura = 268 # Para el caso de problemas C, D
    #paramLectura = 335 # Para el caso de los problemas E, F
    #paramLectura = 668 # Para el caso de los problemas G, H
    
    
    fo = open(dirIn + file ,'r')
    #pesos, matrix = importaMatrix(fo, paramLectura)
    pesos, matrix = importaMatrixRed(fo, paramLectura)
    #pesos, matrix = LeerInstancia(fo)
    return pesos, matrix

# Forma de Uso de esta libreria
#file = 'scpnrg3.txt'
#dirIn= 'C:/Optimization/SCP/OR/G/'
#pesos, matrix = generaMatrix(file,dirIn)
#print pesos, len(pesos)
#print matrix, matrix.shape