__author__ = 'INVESTIGACION'

def obtenerBH_X(BH,X):
    BH_X = list(set(BH) - set(X))
    return BH_X

def obtenerX_BH(BH,X):
    X_BH = list(set(X) - set(BH))
    return X_BH

def getIntersectionBHiX(BH,X):
    BHiX = set(BH).intersection(X)
    return list(BHiX)

def iteraBH_X(BH_X, probabilidadTransicion):
    import numpy as np
    iBH_X = []
    for i in range(0,len(BH_X)):
        aleatorio = np.random.random()
        if aleatorio < probabilidadTransicion[i]:
            iBH_X.append(BH_X[i])
    return iBH_X

def iteraX_BH(X_BH, probabilidadTransicion):
    import numpy as np
    iX_BH = []
    for i in range(0,len(X_BH)):
        aleatorio = np.random.random()
        if aleatorio > probabilidadTransicion[i]:
            iX_BH.append(X_BH[i])
    return iX_BH

def concatenaSolucion(BHiX,iBH_X,iX_BH):

    return sorted(BHiX + iBH_X + iX_BH)

def iterarElemento(lsolucion, BH, probabilidadTransicion):
    BH_X = obtenerBH_X(BH,lsolucion)
    X_BH = obtenerX_BH(BH,lsolucion)
    BHiX = getIntersectionBHiX(BH,lsolucion)
    iBH_X = iteraBH_X(BH_X,probabilidadTransicion)
    iX_BH = iteraX_BH(X_BH,probabilidadTransicion)
    lresult = concatenaSolucion(BHiX,iBH_X,iX_BH)
    return lresult
