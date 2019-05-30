from handleDataset import *
from getKNeighbors import *
from getResponse import *
from getAccuracy import *
from random import randint
import os


def main():

    if os.path.isfile('DadosMetodo01.txt'):  # Se já existir um arquivo de resultados de execuções anteriores
        os.remove('DadosMetodo01.txt')  # este comando o apagará

    if os.path.isfile('DadosMetodo02.txt'):  # Se já existir um arquivo de resultados de execuções anteriores
        os.remove('DadosMetodo02.txt')  # este comando o apagará

    a = 0

    while a < 30:  # Repete todo_o processo 30 vezes
        # Preparando dados
        z1 = []
        z2 = []
        z3 = []

        z12 = []
        z22 = []

        categorias = []

        # MUDAR AO TROCAR BASE %%%%%%%%%%%%%%%%%%%%%%%%%%%%

        base = 'hayes-roth.data'

        categoria = '1'
        categorias.append(categoria)
        categoria = '2'
        categorias.append(categoria)
        categoria = '3'
        categorias.append(categoria)

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        split = 0.6
        k = 1
        T = 15

        handleDataset(base, split, categorias, z1, z2, z3, z12, z22)

        # print(f'z1 inicial: {z1}')

        iteracao1 = 0
        auxk = 2000
        betterk = 0
        auxerros = []
        totalerros = 2000  # Só pra dizer que tem mais do que 0 erros

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MÉTODO 01 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MÉTODO 01 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MÉTODO 01 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        while iteracao1 < T and totalerros > 0:
            # print(f'\n>>>>>>> Iteração: {iteracao1} <<<<<<<')

            while k < 36 and iteracao1 == 0:  # MELHOR K | olha 18 vezes | Só executa na primeira iteração de T

                # Gerando previsões
                predictions = []

                for x in range(len(z2)):
                    neighbors = getKNeighbors(z1, z2[x], k)
                    result = getResponse(neighbors)
                    predictions.append(result)
                    # print('> previsto=' + repr(result) + ', correto=' + repr(z2[x][-1]))

                accuracy = getAccuracy(z2, predictions)

                if accuracy[1] < auxk:
                    auxk = accuracy[1]
                    betterk = k
                    auxkacerto = accuracy[0]
                    auxkerro = auxk
                    auxkacuracia = round(accuracy[2], 2)
                    auxerros.clear()
                    auxerros.append(accuracy[3])

                k = k + 2

            if iteracao1 == 0:

                k = betterk

                """
                print('%%%%%%%%%% MELHOR K %%%%%%%%%%%%')
                print(f'Melhor k: {betterk}')
                print(f'Classificações corretas: {auxkacerto}')
                print(f'Classificações incorretas: {auxkerro}')
                print(f'Acurácia: {auxkacuracia}%')
                print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                """

            # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% T = 0,1,2,...

            # Gerando previsões

            predictions = []

            for x in range(len(z2)):
                neighbors = getKNeighbors(z1, z2[x], k)
                result = getResponse(neighbors)
                predictions.append(result)
                # print('> previsto=' + repr(result) + ', correto=' + repr(z2[x][-1]))
            accuracy = getAccuracy(z2, predictions)

            if iteracao1 > 0:
                """
                print('\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                print(f'K: {k}')
                print(f'Classificações corretas: {accuracy[0]}')
                print(f'Classificações incorretas: {accuracy[1]}')
                print(f'Acurácia: {round(accuracy[2], 2)}%')
                print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')
                """

            auxerros.clear()
            auxerros.append(accuracy[3])

            # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% T = 0,1,2,...

            auxzx = auxerros[0]  # [('Iris-versocolor')]
            totalerros = len(auxzx)  # Total de erros da lista auxerros (int)
            auxza = []

            if totalerros > 0:  # sÓ ENTRA SE HOUVER ERROS

                # print(f'Todos os erros em z2: {auxerros}\n')

                auxza.append(auxerros[0])

                y = 0  # Se tiver 0 erros não entra nesse while
                auxi1 = []
                if totalerros > 1:
                    algerros = int(totalerros / 2)
                else:
                    algerros = totalerros

                while y < algerros:  # PERCORRE METADE DO TOTAL DE ERRROS
                    auxi1 = auxza[0]  # [('3', 5), ('3', 6)]
                    auxi2 = auxi1[y]  # ('3', 5)
                    trocou = 0
                    percorrez1 = 0

                    while percorrez1 < len(z1) and trocou == 0:  # Percorre z1 até encontrar o rótulo e trocar
                        if trocou == 0:
                            randomint = randint(0, (len(z1) - 1))  # Gera 1 inteiro aleatório de 0 a tam z1-1
                            # print(f'Comparação: Z2:{z2[auxi2[1]][-1]} e Z1:{z1[randomint][-1]}')  # Compara z1 e z2
                            if z1[randomint][-1] == auxi2[0]:
                                auxtroca = z2[auxi2[1]]
                                z2[auxi2[1]] = z1[randomint]
                                z1[randomint] = auxtroca
                                trocou = 1
                                # print(f'TROQUEI Z1 E Z2!! \o/\o/\n')
                        percorrez1 += 1
                    y += 1
            else:
                # print('Nenhum erro encontrado\n')
                auxi1 = ''

            iteracao1 += 1
        melhorZ1metodo1 = z1
        melhorKmetodo1 = k
        errosmetodo1 = auxi1
        iteracaometodo1 = iteracao1

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MÉTODO 02 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MÉTODO 02 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MÉTODO 02 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        iteracao1 = 0
        auxk = 2000
        betterk = 0
        auxerros = []
        totalerros = 2000  # Só pra dizer que tem mais do que 0 erros

        k = 1
        T = 15

        while iteracao1 < T and totalerros > 0:
            # print(f'\n>>>>>>> Iteração: {iteracao1} <<<<<<<')
            while k < 36:  # MELHOR K | olha 18 vezes | Executa em todas as iterações de T

                # Gerando previsões
                predictions = []

                for x in range(len(z22)):
                    neighbors = getKNeighbors(z12, z22[x], k)
                    result = getResponse(neighbors)
                    predictions.append(result)
                    # print('> previsto=' + repr(result) + ', correto=' + repr(z2[x][-1]))

                accuracy = getAccuracy(z22, predictions)

                if accuracy[1] < auxk:
                    auxk = accuracy[1]
                    betterk = k
                    auxkacerto = accuracy[0]
                    auxkerro = auxk
                    auxkacuracia = round(accuracy[2], 2)
                    auxerros.clear()
                    auxerros.append(accuracy[3])

                k = k + 2

            k = betterk

            """
            print('%%%%%%%%%% MELHOR K %%%%%%%%%%%%')
            print(f'Melhor k: {betterk}')
            print(f'Classificações corretas: {auxkacerto}')
            print(f'Classificações incorretas: {auxkerro}')
            print(f'Acurácia: {auxkacuracia}%')
            print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            """

            auxzx = auxerros[0]  # [('Iris-versocolor')]
            totalerros = len(auxzx)  # Total de erros da lista auxerros (int)
            auxza = []

            if totalerros > 0:  # SÓ ENTRA SE HOUVER ERROS

                # print(f'Todos os erros em z22: {auxerros}\n')

                auxza.append(auxerros[0])

                y = 0
                auxi1 = []
                if totalerros > 1:
                    algerros = int(totalerros / 2)
                else:
                    algerros = totalerros

                while y < algerros:  # PERCORRE METADE DO TOTAL DE ERRROS
                    auxi1 = auxza[0]  # [('3', 5), ('3', 6)]
                    auxi2 = auxi1[y]  # ('3', 5)
                    trocou = 0
                    percorrez1 = 0

                    while percorrez1 < len(z12) and trocou == 0:  # Percorre z12 até encontrar o rótulo e trocar
                        if trocou == 0:
                            randomint = randint(0, (len(z12) - 1))  # Gera 1 inteiro aleatório de 0 a tam z1-1
                            # print(f'Comparação: Z22:{z22[auxi2[1]][-1]} e Z12:{z12[randomint][-1]}')  # Compara z12 e z22
                            if z12[randomint][-1] == auxi2[0]:
                                auxtroca = z22[auxi2[1]]
                                z22[auxi2[1]] = z12[randomint]
                                z12[randomint] = auxtroca
                                trocou = 1
                                # print(f'TROQUEI Z12 E Z22!! \o/\o/\n')
                        percorrez1 += 1
                    y += 1
            else:
                # print('Nenhum erro encontrado\n')
                auxi1 = ''

            iteracao1 += 1

        melhorZ1metodo2 = z12
        melhorKmetodo2 = k
        errosmetodo2 = auxi1
        iteracaometodo2 = iteracao1

        """
        print('>>>>> MÉTODO 01 <<<<<')
        print(f'z1: {melhorZ1metodo1}')
        print(f'Melhor K inicial: {melhorKmetodo1}')
        print(f'T Iterações: {iteracaometodo1}')
        print(f'QTD Erros: {len(errosmetodo1)}')
        print(f'Erros: {errosmetodo1}')

        print('>>>>> MÉTODO 02 <<<<<')
        print(f'z1: {melhorZ1metodo2}')
        print(f'Melhor K do melhor Z1: {melhorKmetodo2}')
        print(f'T Iterações: {iteracaometodo2}')
        print(f'QTD Erros: {len(errosmetodo2)}')
        print(f'Erros: {errosmetodo2}')
        """

        # %%%%%%%%%%%%%%%%%%%%%%%% Comparação entre métodos %%%%%%%%%%%%%%%%%%%%%%%%
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%% APLICAÇÃO EM Z3 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        # %%%%%% APLICANDO O MÉTODO 01 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        predictions = []

        for x in range(len(z3)):
            neighbors = getKNeighbors(melhorZ1metodo1, z3[x], melhorKmetodo1)
            result = getResponse(neighbors)
            predictions.append(result)
            # print('> previsto=' + repr(result) + ', correto=' + repr(z3[x][-1]))

        accuracy = getAccuracy(z3, predictions)

        auxk = accuracy[1]
        qtdacertos = accuracy[0]
        qtderros = auxk
        auxkacuracia = round(accuracy[2], 2)
        auxerros.clear()
        auxerros.append(accuracy[3])

        auxzx = auxerros[0]  # [('Iris-versocolor')]

        print('\n>>>>>>>>>>> MÉTODO 01 <<<<<<<<<<<')
        print(f'Iteração confiança: {a+1}')  # Trocar!!
        print(f'Melhor K inicial: {melhorKmetodo1}')
        print(f'Melhor z1: {melhorZ1metodo1}')
        print(f'T Iterações de troca (z1/z2): {iteracaometodo1}')
        print(f'Classificações corretas em z3 (Acertos): {qtdacertos}')
        print(f'Classificações incorretas em z3 (Erros): {qtderros}')
        print(f'Lista de Erros em z3: {auxzx}')
        print(f'Acurácia: {auxkacuracia}%')
        print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')

        with open('DadosMetodo01.txt', mode='a') as fm1:
            writer = csv.writer(fm1)
            linhasm1 = [a+1, melhorKmetodo1, qtdacertos, qtderros, auxkacuracia]
            writer.writerow(linhasm1)

        # %%%%%% APLICANDO O MÉTODO 02 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        predictions = []

        for x in range(len(z3)):
            neighbors = getKNeighbors(melhorZ1metodo2, z3[x], melhorKmetodo2)
            result = getResponse(neighbors)
            predictions.append(result)
            # print('> previsto=' + repr(result) + ', correto=' + repr(z3[x][-1]))

        accuracy = getAccuracy(z3, predictions)

        auxk = accuracy[1]
        qtdacertos = accuracy[0]
        qtderros = auxk
        auxkacuracia = round(accuracy[2], 2)
        auxerros.clear()
        auxerros.append(accuracy[3])

        auxzx = auxerros[0]  # [('Iris-versocolor')]

        print('\n>>>>>>>>>>> MÉTODO 02 <<<<<<<<<<<')
        print(f'Iteração confiança: {a+1}')  # Trocar!!
        print(f'Melhor K do melhor Z1: {melhorKmetodo2}')
        print(f'Melhor z1: {melhorZ1metodo2}')
        print(f'T Iterações de troca (z1/z2): {iteracaometodo2}')
        print(f'Classificações corretas em z3 (Acertos): {qtdacertos}')
        print(f'Classificações incorretas em z3 (Erros): {qtderros}')
        print(f'Lista de Erros em z3: {auxzx}')
        print(f'Acurácia: {auxkacuracia}%')
        print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')

        with open('DadosMetodo02.txt', mode='a') as fm2:
            writer = csv.writer(fm2)
            linhasm2 = [a+1, melhorKmetodo2, qtdacertos, qtderros, auxkacuracia]
            writer.writerow(linhasm2)

        a += 1


main()
