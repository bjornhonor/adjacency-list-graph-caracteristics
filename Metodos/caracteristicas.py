'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Bruno Penteado Carrara

caracteristicas - Funções para obtenção das características do grafo e operações em uma matriz de adjacências.

12/09/2022  
===================================================='''

from collections import defaultdict
import numpy as np


'''Descrição: Cria uma lista de adjacências de um grafo representado por uma matriz de adjacências.
Entrada: matriz de adjacências (arquivo .txt)
Saída: lista de adjacências (tipo Dictionary)'''
def criaListaAdjacencias(matriz):
    listaAdj = defaultdict(list)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > 0:
                k = matriz[i][j]
                for n in range(k):
                    listaAdj[i].append(j)
    return listaAdj

'''Descrição: Verifica se os vértices vi e vj são adjacentes.
Entrada: lista de adjacências (tipo Dictionary), vi e vj (ambos números inteiros que indica o id do vértice)
Saída: Boolean (True se os vértices são adjacentes; False caso contrário)'''
def verificaAdjacencia(listaAdj, vi, vj):
    tipo = tipoGrafo(listaAdj)
    if tipo == 1:
        linha = listaAdj[vi]
        verticesAdjacentes = False
        for i in range(len(linha)):
            if vj == linha[i]:
                return True
        
        linha = listaAdj[vj]
        for j in range(len(linha)):
            if vi == linha[j]:
                return True
    else:
        linha = listaAdj[vi]
        verticesAdjacentes = False
        for i in range(len(linha)):
            if vj == linha[i]:
                verticesAdjacentes = True


    print('Vertices', vi, 'e', vj, 'são adjacentes?', verticesAdjacentes, '\n')
    return verticesAdjacentes

'''Descrição: Retorna se uma dada matriz é simetrica.
Entrada: matriz de adjacências
Saída: Boolean(True - matriz simetrica; False - matriz assimetrica)'''
def isSimetrica(listaAdj):
    for i in listaAdj:
        valores = listaAdj[i]
        for j in range(len(valores)):
            k = 0
            if valores[j] > i:
                for n in range(len(listaAdj[valores[j]])):
                    valores2 = listaAdj[valores[j]]
                    if valores2[n] == i:
                        k = 1
                if k == 0:
                    return False
    return True

'''Descrição: Retorna se uma dada matriz possui aresta em um unico vertice (tem valor na diagonal).
Entrada: matriz de adjacências
Saída: Boolean(True - possui aresta em um so vertice; False - nao possui aresta em um so vertice)'''
def temDiagonal(listaAdj):
    for i in listaAdj:
        valores = listaAdj[i]
        for j in range(len(valores)):
            if valores[j] == i:
                return True
    return False

'''Descrição: Retorna se uma dada matriz é simples ou representa um multigrafo.
Entrada: matriz de adjacências
Saída: Boolean(True - possui uma aresta por conexao entre vertices; False - possui mais de uma aresta por conexao de vertices)'''
def isSimple(listaAdj):
    for i in listaAdj:
        valores = listaAdj[i]
        for j in range(len(valores)-1):
            if valores[j] == valores[j+1]:
                return False
    return True

'''Descrição: Retorna o tipo do grafo representado por uma dada lista de adjacências.
Entrada: lista de adjacências (tipo Dictionary)
Saída: Integer (0 – simples; 1 – dígrafo; 2 – multigrafo; 3 – pseudografo)'''
def tipoGrafo(listaAdj):
    tipo = 0
    simetrica = isSimetrica(listaAdj)
    diagonal = temDiagonal(listaAdj)
    simples = isSimple(listaAdj)
    if simetrica == False:
        tipo = 1
    elif diagonal == True:
        tipo = 3
    elif simples == False:
        tipo = 2
    return tipo

'''Descrição: Retorna quantas arestas possui um dado grafo.
Entrada: matriz de adjacências
Saída: Float(quantidade de arestas de um grafo)'''
def contaArestas(listaAdj):
    tipo = tipoGrafo(listaAdj)
    numArestas = 0
    if tipo == 1: # para grafos direcionados, apenas somamos os valores da lista
        for i in listaAdj:
            numArestas += len(listaAdj[i])

    elif tipo == 3: # para pseudografos, calculamos o valor da diagonal e retiramos da soma total, entao dividimos por 2
        soma = 0 # para tirar a simetria e apos isso somamos o valor da diagonal novamente

        for i in listaAdj:
            valores = listaAdj[i]
            for j in range(len(valores)):
                if valores[j] == i:
                    soma += 1
        for i in listaAdj:
            numArestas += len(listaAdj[i])
        numArestas = (numArestas - soma) / 2
        numArestas += soma

    else: # para os outros tipos de grafos, basta somarmos os valores das posicoes da listaAdj e dividir por 2 para tirar a simetria
        for i in listaAdj:
            numArestas += len(listaAdj[i])
        numArestas = numArestas/2
    return numArestas

'''Descrição: Retorna o valor da densidade do grafo.
Entrada: lista de adjacências (tipo Dictionary)
Saída: Float (valor da densidade com precisão de três casas decimais)'''
def calcDensidade(listaAdj):
    densidade = 0
    qtdVertices = len(listaAdj) # numero de vertices
    qtdEdges = contaArestas(listaAdj)
    # print(qtdEdges)
    if tipoGrafo(listaAdj) == 1: #grafo direcionado
        densidade = qtdEdges / (qtdVertices * (qtdVertices - 1)) # formula para digrafo
    else:
        densidade = (2 * qtdEdges) / (qtdVertices * (qtdVertices - 1)) # formula para grafos nao direcionados
    return densidade

'''Descrição: Insere uma aresta no grafo considerando o par de vértices vi e vj.
Entrada: lista de adjacências (tipo Dictionary), vi e vj (ambos são números inteiros que indicam o id do vértice)
Saída: lista de adjacências (tipo Dictionary) com a aresta inserida.'''
def insereAresta(listaAdj, vi, vj):
    tipo = tipoGrafo(listaAdj)
    if tipo == 1: # se for digrafo
        listaAdj[vi].append(vj) # adiciona o vertice na linha desejada
    
    elif vi == vj:
        listaAdj[vi].append(vj) # ser for uma aresta de um so vertice nao precisa de simetria

    else: # se for qualquer grafo que nao seja direcionado
        listaAdj[vi].append(vj) # soma 1 aresta, podendo iniciar uma aresta ou transformar em multigrafo, adicionando mais uma aresta
        listaAdj[vj].append(vi) # mesma operacao, mas para deixar a lista simetrica
    print('Aresta entre os pontos', vi, 'e', vj, 'criada com sucesso', '\n')    
    return listaAdj

'''Descrição: Remove uma aresta do grafo considerando o par de vértices vi e vj.
Entrada: lista de adjacências (tipo Dictionary), vi e vj (ambos são números inteiros que indicam os ids dos vértices)
Saída: lista de adjacências (tipo Dictionary) com a aresta removida.'''
def removeAresta(listaAdj, vi, vj):
    tipo = tipoGrafo(listaAdj)

    if tipo == 1: # se for digrafo
        listaAdj[vi].remove(vj) #remove o valor de vj na linha de vi

    elif vi == vj:
        listaAdj[vi].remove(vj) # se for uma aresta de um so vertice nao precisa ser simetrico

    else: # se for qualquer grafo que nao seja direcionado
        listaAdj[vi].remove(vj) # subtrai 1 aresta, podendo retirar uma aresta de um multagrafo, ou apenas remover a aresta
        listaAdj[vj].remove(vi) # mesma operacao, mas para deixar a lista simetrica

    print('Aresta entre os pontos', vi, 'e', vj, 'removida com sucesso', '\n')
    return listaAdj

'''Descrição: Insere um vértice no grafo.
Entrada: lista de adjacências (tipo Dictionary), vi (número inteiro que indica o id do vértice)
Saída: lista de adjacências (tipo Dictionary) com o vértice inserido.'''
def insereVertice(listaAdj, vi):
    listaAdj[vi] = []
    print('vertice', vi, "adicionado no grafo!")
    return listaAdj

'''Descrição: Remove um vértice do grafo.
Entrada: lista de adjacências (tipo Dictionary), vi (número inteiro que indica o id do vértice)
Saída: lista de adjacências (tipo Dictionary) com o vértice removido.'''
def removeVertice(listaAdj, vi):
    
    for i in listaAdj:
        valores = listaAdj[i]
        for j in range(len(listaAdj[i])):
            if valores[j] == vi:
                listaAdj[i].remove(vi) # se for igual remove

    listaAdj.pop(vi)

    print('vertice', vi, 'removido do grafo')
    return listaAdj
    
    







