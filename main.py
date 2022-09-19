'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Bruno Penteado Carrara

Grafos - Programa com funções básicas para práticas de algoritmos em grafos.
Classe principal - desenvolvido em Python 3.10.6

12/09/2022
===================================================='''

import sys
from igraph import *
from Inicializacao import (dataSet as ds, grafo as g, visualizacao as vis)
from Metodos import (caracteristicas as car)

'''Core do programa'''
def main(instancia):

    matriz = ds.criaMatrizAdjacencias(instancia)
    # print(matriz, '\n') # '\n' para inserir linha em branco ao final do comando

    listaAdj = car.criaListaAdjacencias(matriz)
    for i in listaAdj:
        print(i,':', listaAdj[i], '\n')

    G = g.criaGrafo(matriz)
    print(G, '\n') # Mostra as características do grafo.

    vis.visualizarGrafo(True, G)  # True para visualização do grafo ou False.
    tipo = car.tipoGrafo(listaAdj)
    if tipo == 0:
        print('simples')
    elif tipo == 1:
        print('digrafo')
    elif tipo == 2:
        print('multigrafo') 
    else:
        print('pseudografo')

    isAdjacente = car.verificaAdjacencia(listaAdj, 0, 1)

    densidade = car.calcDensidade(listaAdj)
    t = 3
    d = int(densidade * 10**t)/10**t
    print('Densidade do grafo:', d, '\n')

    for i in listaAdj:
        print(i,':', listaAdj[i], '\n')

    # listaAdj = car.insereAresta(listaAdj, 0, 1) # insere aresta
    # listaAdj = car.removeAresta(listaAdj, 0, 1) # remove aresta
    # listaAdj = car.insereVertice(listaAdj, 4) # insere vertice
    listaAdj = car.removeVertice(listaAdj, 3) # remove vertice

    for i in listaAdj:
        print(i,':', listaAdj[i], '\n')

    resultado = [instancia, tipo, isAdjacente, d] # Lista de tipo misto com valores dos resultados
    ds.salvaResultado(resultado) # Salva resultado em arquivo

'''Chamada a função main()
   Argumento Entrada: [1] dataset'''
if __name__ == '__main__':
    main(str(sys.argv[1]))

