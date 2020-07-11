from copy import deepcopy
import solution as sl
import setCovering as sC
import numpy  as np


def realizaStandarLocalSearch(best,matrix,p,rHeuristic,dictcHeuristics,dict,cHeuristic):
    # El primer paso es obtener el complemento de BHz, que corresponde a los que se insertan
    BHtemp = deepcopy(best)
    BHFinal = deepcopy(best)
    contador = 0
    for i in best:

        BHtemp.remove(i)
        solutionT = deepcopy(sl.generaSolucion(BHtemp,matrix,p,rHeuristic,dictcHeuristics,dict,cHeuristic))
        solutionT = sC.mejoraSolucion(solutionT,matrix)
        BHFinal = deepcopy(getBestSolution(BHFinal,solutionT,p))

        else:
            contador = contador + 1
    complement = list(set(range(0,1000)) - set(best))
    for i in complement:
        Option = np.random.randint(1,4)
        BHtemp.append(i)
        if Option == contador:
            solutionT = deepcopy(sl.generaSolucion(BHtemp,matrix,p,rHeuristic,dictcHeuristics,dict,cHeuristic))
            solutionT = sC.mejoraSolucion(solutionT,matrix)
            BHFinal = deepcopy(getBestSolution(BHFinal,solutionT,p))
            contador = 0
        else:
            contador = contador + 1

    return BHFinal


def getBestSolution(BHFinal, BHtemp,p):

    if sC.fitnessFunction(BHFinal,p) > sC.fitnessFunction(BHtemp,p):
        print 'Ehhhhhh',sC.fitnessFunction(BHtemp,p)
        BHFinal = deepcopy(BHtemp)
    return BHFinal



def realizaLocalSearch(best,matrix,p,rHeuristic,dictcHeuristics,dict,cHeuristic):
    # BH solo tiene el vector
    BHtemp = deepcopy(best)
    BHFinal = deepcopy(best)
    lcandidatos = list(set(range(0,len(p))) - set(best))

    for i in range(0,len(BHtemp)):
        for j in range(0,len(lcandidatos)):
            #print 'Removiendo', temp, i,j
            BHtemp.remove(BHtemp[i])
            BHtemp.append(lcandidatos[j])
            solutionT = deepcopy(sl.generaSolucion(BHtemp,matrix,p,rHeuristic,dictcHeuristics,dict,cHeuristic))
            solutionT = sC.mejoraSolucion(solutionT,matrix)
            solutionT = deepcopy(getBestSolution(BHFinal,solutionT,p))
            if sC.fitnessFunction(BHtemp,p) < sC.fitnessFunction(BHFinal,p): # Vamos a comparar
                BHFinal = deepcopy(BHtemp)
                temp = deepcopy(best)
                print 'ehhh entro funciona', BHFinal
            else:
                #print 'BH', BH
                temp = deepcopy(best)
    return BHFinal
