"""
Etapa 3: encontre o ponto k mais próximo
Agora que você calculou a distância de cada ponto, podemos usá-lo para coletar
os k pontos / instâncias mais semelhantes para os dados / instâncias de teste
fornecidos.

Este é um processo simples: Calcule a distância em toda a instância e selecione
o subconjunto que tem a menor distância euclidiana.

Vamos criar uma função getKNeighbors que retorne k vizinhos mais semelhantes
do conjunto de treinamento para uma determinada instância de teste.
"""

import operator
from euclideanDistance import *


def getKNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

"""
# Testando a função getKNeighbors.


trainSet = [[2, 2, 2, 'a'], [4, 4, 4, 'b'], [1, 1, 1, 'c'], [6, 6, 6, 'd']]
testInstance = [5, 5, 5]
k = 1
neighbors = getKNeighbors(trainSet, testInstance, k)
print(neighbors)
"""