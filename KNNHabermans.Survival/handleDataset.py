import csv
import random


def handleDataset(filename, split, categorias, z1=[], z2=[], z3=[], z12=[], z22=[]):
    with open(filename, 'r') as f:
        lines = csv.reader(f)  # linhas
        dataset = list(lines)
        totalcol = len(dataset[0][:])  # descobre qtd colunas da linha

        rot0 = 0
        rot1 = 0

        z1aux0 = 1
        z1aux1 = 1

        z2aux0 = 1
        z2aux1 = 1

        z3aux0 = 1
        z3aux1 = 1

        aux = 0

        for x in range(len(dataset)):  # x(0 a 149)

            # Transforma os campos de cada linha em float, exceto o último (categoria)
            for y in range(totalcol - 1):
                dataset[x][y] = float(dataset[x][y])

# MUDAR AO TROCAR BASE %%%%%%%%%%%%%%%%%%%%%%%%%%%%

            # Totais de cada rótulo
            if (dataset[x].count(categorias[0])) == 1:
                rot0 += 1
            elif (dataset[x].count(categorias[1])) == 1:
                rot1 += 1

        # Quantidade máxima de cada rótulo para Treinamento/Avaliação juntos
        maxrotulo0 = int(split * rot0)
        maxrotulo1 = int(split * rot1)

        # Quantidade total de cada rótulo para Z1
        # ex: 25/2 = 12
        z1totalrotulo0 = int(maxrotulo0 / 2)
        z1totalrotulo1 = int(maxrotulo1 / 2)

        # Quantidade total de cada rótulo para Z2
        # ex: 50-25-12 = 13
        z2totalrotulo0 = int((maxrotulo0 - z1totalrotulo0))
        z2totalrotulo1 = int((maxrotulo1 - z1totalrotulo1))

        # Quantidade total de cada rótulo para Z3
        # ex: 50-(12+13) = 25
        z3totalrotulo0 = int(rot0 - (z1totalrotulo0 + z2totalrotulo0))
        z3totalrotulo1 = int(rot1 - (z1totalrotulo1 + z2totalrotulo1))

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        random.shuffle(dataset)  # Embaralho minha lista inteira

        for x in range(len(dataset)):  # x(0 a 149 = 150)

# MUDAR AO TROCAR BASE %%%%%%%%%%%%%%%%%%%%%%%%%%%%

            # Z1----------
            if (dataset[x].count(categorias[0])) == 1 and z1aux0 <= z1totalrotulo0:
                z1aux0 += 1
                z1.append(dataset[x])
                z12.append(dataset[x])

            elif (dataset[x].count(categorias[1])) == 1 and z1aux1 <= z1totalrotulo1:
                z1aux1 += 1
                z1.append(dataset[x])
                z12.append(dataset[x])

            # Z2----------
            elif (dataset[x].count(categorias[0])) == 1 and z2aux0 <= z2totalrotulo0:
                z2aux0 += 1
                z2.append(dataset[x])
                z22.append(dataset[x])

            elif (dataset[x].count(categorias[1])) == 1 and z2aux1 <= z2totalrotulo1:
                z2aux1 += 1
                z2.append(dataset[x])
                z22.append(dataset[x])

            # Z3----------
            elif (dataset[x].count(categorias[0])) == 1 and z3aux0 <= z3totalrotulo0:
                z3aux0 += 1
                z3.append(dataset[x])

            elif (dataset[x].count(categorias[1])) == 1 and z3aux1 <= z3totalrotulo1:
                z3aux1 += 1
                z3.append(dataset[x])

            else:
                aux += 1
                print(f'Problema!! Sobraram {aux} instâncias sem conjunto.')

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

"""
# Testando a função handleDataset


z1 = []
z2 = []
z3 = []
categorias = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
# Este 0.6 é a porcentagem geral da mostra para treinamento/avaliação
handleDataset('iris.data', 0.6, categorias, 3, z1, z2, z3)

print('........')
print('z1 txt: ' + repr(len(open('z1.txt', 'r').readlines())))
print('z2 txt: ' + repr(len(open('z2.txt', 'r').readlines())))
print('z3 txt: ' + repr(len(open('z3.txt', 'r').readlines())))
print('........')
print('z1 mem: ' + repr(len(z1)))
print('z2 mem: ' + repr(len(z2)))
print('z3 mem: ' + repr(len(z3)))
"""
