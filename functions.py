import numpy as np
import os

def get_recursos_totais(qtd_tipos_recursos):
    recursos_totais = np.zeros((qtd_tipos_recursos), dtype='int64')
    for i in range(qtd_tipos_recursos):
        recurso = int(input('Digite a quantidade do recurso %d:\n'
                            '>>> ' % (i+1)))
        recursos_totais[i] += recurso

    print('\nVetor de recursos totais (E):', recursos_totais)
    print()

    return recursos_totais


def get_matriz_alocados(qtd_processos, qtd_tipos_recursos):
    matriz_alocados = np.zeros((qtd_processos, qtd_tipos_recursos), dtype='int64')
    for i in range(len(matriz_alocados)):
        for j in range(len(matriz_alocados[i])):
            matriz_alocados[i, j] += int(input('Digite a quantidade do recurso %d alocada no processo %d:\n' \
                                               '>>> ' % ((j + 1), (i + 1))))
     
    print('\nMatriz de recursos alocados a cada processo (C):\n', matriz_alocados)
    print()

    return matriz_alocados


def get_vetor_recursos_alocados(matriz_alocados):
    recursos_alocados = np.zeros(len(matriz_alocados[0]), dtype='int64')
    for i in range(len(matriz_alocados)):
        for j in range(len(matriz_alocados[i])):
            recursos_alocados[j] += matriz_alocados[i, j]

    print('\nVetor de recursos alocados (P):\n', recursos_alocados)
    print()

    return recursos_alocados


def get_vetor_recursos_disponiveis(recursos_totais, recursos_alocados):
    recursos_disponiveis = recursos_totais - recursos_alocados
    print('\nVetor de recursos disponíveis (A):\n', recursos_disponiveis)
    print()
    
    return recursos_disponiveis


def get_matriz_recursos_necessarios(qtd_processos, qtd_tipos_recursos):
    matriz_recursos_necessarios = np.zeros((qtd_processos, qtd_tipos_recursos), dtype='int64')
    for i in range(qtd_processos):
        for j in range(qtd_tipos_recursos):
            recurso_necessario = int(input('Digite a quantidade do recurso %d que é necessário ao processo %d:\n' \
                                           '>>> ' % ((j + 1), (i + 1))))
            matriz_recursos_necessarios[i, j] += recurso_necessario

    print('\nMatriz de recursos necessarios a cada processo (R):\n', matriz_recursos_necessarios)
    print()

    return matriz_recursos_necessarios


def imprimir_os_dados(recursos_totais, matriz_alocados, recursos_alocados, recursos_disponiveis, matriz_recursos_necessarios):
    print('Recursos totais (E):\n', recursos_totais)
    print()
    print('Recursos alocados a cada processo (C):\n', matriz_alocados)
    print()
    print('Vetor de recursos alocados (P):\n', recursos_alocados)
    print()
    print('Vetor de recursos disponiveis (A):\n', recursos_disponiveis)
    print()
    print('Matriz de recursos necessarios (R):\n', matriz_recursos_necessarios)
    print()
    input('Pressione Enter para continuar.....')
    os.system('clear')


def algoritmo_banqueiro(qtd_processos,qtd_tipos_recursos, recursos_disponiveis, matriz_recursos_necessarios, matriz_alocados):

    # Vetor com 1's em cada processo, indicando se este ainda irá rodar (n = 1) ou não (n = 0)

    rodando = np.ones(qtd_processos, dtype='int64')

    # enquanto a quantidade de números diferentes de 0 for maior do que 0, a linha de código do while irá rodar

    while np.count_nonzero(rodando) > 0:
        alocou_recursos = False
        for num_processo in range(qtd_processos):

            # se o processo de índice "num_processo" irá rodar ou não

            if rodando[num_processo] != 0:
                if all(i >= 0 for i in recursos_disponiveis - (matriz_recursos_necessarios[num_processo] - matriz_alocados[num_processo])):
                    alocou_recursos = True
                    print('Processo %d está rodando' % (num_processo + 1))
                    input('Pressione Enter para prosseguir......\n')
                    rodando[num_processo] = 0
                    recursos_disponiveis += matriz_alocados[num_processo]
                    matriz_alocados[num_processo] = np.zeros(qtd_tipos_recursos, dtype='int64')
                    print("Recursos Disponíveis (A):\n", recursos_disponiveis)
                    print()
                    print("Recursos Necessários (R):\n", matriz_alocados)
                    print()

        if alocou_recursos == False:
            print('Os processos entrarão em Deadlock')
            exit()

    print('Os processos não entrarão em Deadlock.')