"""
Etapa 4: Prever a classe
Agora que você tem os k pontos / vizinhos mais próximos para a instância de
teste, a próxima tarefa é a resposta prevista com base nesses vizinhos.

Você pode fazer isso permitindo que cada vizinho vote em seu atributo de
classe e obtenha a maioria como a previsão.

Vamos criar uma função getResponse para obter a maioria votada como resposta
de vários vizinhos.
"""

import operator


def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

"""
# Testando a função getResponse


neighbors = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
print(getResponse(neighbors))
"""