__author__ = 'INVESTIGACION'

from numpy import zeros
from sklearn.cluster import KMeans
import numpy as np
import math

def obtieneProbabilidades(lDelta):
    lprobabilidades = zeros(len(lDelta))
    for i in range(0,len(lDelta)):
        T = 1/(1+math.exp(-1*lDelta[i]/2))
        lprobabilidades[i] = T
    return lprobabilidades