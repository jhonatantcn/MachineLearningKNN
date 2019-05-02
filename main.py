from handleDataset import *
from getKNeighbors import *
from getResponse import *
from getAccuracy import *


def main():
    # TESTANDO O CLASSIFICADOR
    # Preparando dados
    trainingSet = []
    testSet = []
    split = 0.67
    handleDataset('iris.data', split, trainingSet, testSet)
    print('Train set: ' + repr(len(trainingSet)))
    print('Test set: ' + repr(len(testSet)))
    # Gerando previsões
    predictions = []
    k = 3
    for x in range(len(testSet)):
        neighbors = getKNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('> prevista=' + repr(result) + ', correta=' + repr(testSet[x][-1]))

    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')


main()
