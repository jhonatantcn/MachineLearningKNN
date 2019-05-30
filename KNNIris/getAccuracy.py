def getAccuracy(testSet, predictions):
    correto = 0
    incorreto = 0
    errosprev = []

    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:  # Comparação entre real e previsão
            correto += 1
        else:
            incorreto += 1
            erro = testSet[x][-1], x
            errosprev.append(erro)

    return [correto, incorreto, (correto / float(len(testSet))) * 100.0, errosprev]


"""
# Testando a função getAccuracy
# Neste caso dá 66,66% de acerto

testSet = [[1.1,1.1,1.1,'a'], [2.2,2.2,2.2,'a'], [3.2,3.2,3.2,'b']]
predictions = ['a', 'a', 'a']
accuracy = getAccuracy(testSet, predictions)
print(accuracy)
"""
