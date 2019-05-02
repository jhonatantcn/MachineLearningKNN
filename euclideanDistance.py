"""
Etapa 2: calcular a distância
Para fazer quaisquer previsões, você deve calcular a distância entre o novo
ponto e os pontos existentes, pois você precisará de k pontos mais próximos.

Neste caso, para calcular a distância, usaremos a distância euclidiana. Isso
é definido como a raiz quadrada da soma das diferenças quadradas entre as duas
matrizes de números

Especificamente, precisamos apenas dos primeiros 4 atributos (recursos) para o
cálculo da distância, pois o último atributo é um rótulo de classe. Assim, uma
das abordagens é limitar a distância euclidiana a um comprimento fixo, ignorando
assim a dimensão final.

Resumindo, vamos definir a função euclideanDistance como segue:
"""

import math


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)

"""
# Testando a função euclideanDistance,


data1 = [2, 2, 2, 'a']
data2 = [4, 4, 4, 'b']
distance = euclideanDistance(data1, data2, 3)
print ('Distance: ' + repr(distance))
"""