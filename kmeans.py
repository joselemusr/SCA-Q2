__author__ = 'INVESTIGACION'

from numpy import zeros
from sklearn.cluster import KMeans
import numpy as np

def actualizaProbabilidadGrupo(centroides):
    ############################################################################################################################
    # Corresponden a los parametros del Algoritmo
    factorProbabilidad = 0.1
    factorAmplificacion = 1
    probabilidades = [0.05, 0.1, 0.15, 0.20, 0.3]
    ############################################################################################################################
    centroides = centroides[centroides[:, 1].argsort()][::-1]
    for i in range(0,len(centroides)):
        #centroides[i,2] = (i+1)*factorAmplificacion*factorProbabilidad
        centroides[i,2] = probabilidades[i]
    return centroides

def obtieneGrupos(ldelta):
    """
    :param llistaSoluciones: La lista de soluciones
    :return: grupos y centroides, los grupos asociados a la lista y los centroides
    """
    ############################################################################################################################
    # Numero de clusters
    K = 5# Numero de grupos, corresponde a un parametro de la metaheuristica.
    ############################################################################################################################
    centroides = zeros((K,3))
    #X = fitllistaSoluciones[:,1].reshape(-1,1) # Para poder ejecutar adecuadamente el K-means
    X = np.asanyarray(ldelta)
    X = X.reshape(-1,1)

    kmeans = KMeans(n_clusters=K)
    grupos = kmeans.fit_predict(X)
    #print(X)
    centroids = kmeans.cluster_centers_
    # Generamos los centroides con el grupo asociado
    for i in range(0,len(centroids)):
        centroides[i,0] = i
        centroides[i,1] = centroids[i]
    centroides = actualizaProbabilidadGrupo(centroides)
    return grupos, centroides

def obtieneProbabilidades(lgrupos,lcentroides):
    lprobabilidades = zeros(len(lgrupos))
    for i in range(0,len(lgrupos)):
        #print('El tipo de datos de lgurpo',type(lgrupos[i]),lgrupos[i])
        lprobabilidades[i] = lcentroides[int(lgrupos[i]),2]
    return lprobabilidades