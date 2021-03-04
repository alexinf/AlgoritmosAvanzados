#!/usr/bin/python3
# coding: utf-8 

class Grafo(object):

    def __init__(self, adyacencia):
        self.ady = adyacencia
        self._init_grafo(-1)

    def _init_grafo(self, inicio):

        self.encontrado = {}
        self.procesado = {}
        self.padre = {}
        for k in self.ady.keys():
            self.encontrado[k] = False
            self.procesado[k] = False
            self.padre[k] = -1

        self.inicio = inicio
        self.nodos = []

    def profundidad(self, inicio):
 
        self._init_grafo(inicio)
        q = [inicio]
        self.encontrado[inicio] = True
        self.nodos.append(inicio)
        while q:
            v = q.pop()
            self.procesado[v] = True

            for vecino in self.ady[v]:
                if not self.encontrado[vecino]:
                    self.nodos.append(vecino)
                    q.append(vecino)
                    self.encontrado[vecino] = True
                    self.padre[vecino] = v


while True:
    linea = input()
    if linea == '0 0':
        break

    g = int(linea.split()[1:][0])
        
    universidad = {}
    universidad['0'] = []

    for grupo in range(g):
        estudiates = input().split()[1:]
        for est in estudiates:
            if not est in universidad:        
                universidad[est] = []

            auxGrupo = "g"+str(grupo)
                
            if not auxGrupo in universidad:
                universidad[auxGrupo] = []

            universidad[est].append(auxGrupo)
            universidad[auxGrupo].append(est)
    print (universidad)
    inicio = '0'
    g = Grafo(universidad)
    g.profundidad(inicio)
    inf = list(filter( lambda x: not 'g' in x ,g.nodos))
    print(len(inf))