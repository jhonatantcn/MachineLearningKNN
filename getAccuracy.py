"""
Etapa 5: verifique a precisão
Agora que temos todas as partes do algoritmo kNN no lugar. Vamos verificar
a precisão da nossa previsão!

Uma maneira fácil de avaliar a precisão do modelo é calcular uma proporção do
total de predições corretas de todas as previsões feitas.

Vamos criar uma função getAccuracy que soma as previsões corretas totais e
retorna a precisão como uma porcentagem das classificações corretas.
"""


def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] is predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0

"""
# Testando a função getAccuracy


testSet = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
predictions = ['a', 'a', 'a']
accuracy = getAccuracy(testSet, predictions)
print(accuracy)
"""