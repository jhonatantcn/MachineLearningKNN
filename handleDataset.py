"""
Etapa 1: Manipulando os dados
O primeiro passo será lidar com o conjunto de dados da íris.
Abra o conjunto de dados usando a função [open] e leia as linhas de dados
com a função [reader] disponível no módulo csv.

Agora você precisa dividir os dados em um conjunto de dados de treinamento
(para fazer a previsão) e em um conjunto de dados de teste (para avaliar a
precisão do modelo).

Antes de continuar, converta as medidas de flor carregadas como seqüências
de caracteres em números. Em seguida, divida aleatoriamente o conjunto de
dados em trem e teste o conjunto de dados. Geralmente, uma proporção padrão
de 67/33 é usada para teste / divisão de trem

Adicionando tudo, vamos definir uma função handleDataset que carregará o CSV
quando fornecido com o nome exato do arquivo e o dividirá aleatoriamente em
conjuntos de dados de treinamento e teste usando a taxa de divisão fornecida.
"""

import csv
import random

"""
# Código que imprime todas as linhas do arquivo
with open(r'/home/jhonatan/PycharmProjects/project01/iris.data') as csvfile:
    lines = csv.reader(csvfile)
    for row in lines:
        print (', '.join(row))
"""


def handleDataset(filename, split, trainingSet=[], testSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

"""
# Testando a função handleDataset,


trainingSet = []
testSet = []
# Este 0,66 é a porcentagem geral da mostra para treinamento
handleDataset(r'iris.data', 0.66, trainingSet, testSet)
print('Train: ' + repr(len(trainingSet)))
print('Test: ' + repr(len(testSet)))
"""