#!/usr/bin/python3
# coding: utf-8 
# Fidel Alexander Marquez

from collections import deque

emp = []
vis = []

class Par:
    def __init__(self,destino,costo):
        self.destino = destino
        self.costo = costo

    def getDestino(self):
        return self.destino

    def getPeso(self):
        return  self.costo

class Grafo:

    def __init__(self, v):
        self.grafo = [ None for i in range(v)]
        self.parejas = {}

    def anadirArista(self, origen, destino, peso):

        if self.grafo[origen]==None:
            self.grafo[origen]=[]

        self.grafo[origen].append(Par(destino,peso))


    def grado(self,vertice):
        grado=0

        if self.grafo[vertice]!=None:
            grado = len(self.grafo[vertice])

        return grado

    def getVecinos(self, v):
        vecinos = []
        if self.grafo[v]!=None:
            vecinos=self.grafo[v];

        return vecinos

    # recorrido en amplitud
    def  bfs(self, inicio):
        orden = []

        marcado = [ False for i in range(len(self.grafo))]
        estructura = deque()

        estructura.append(inicio)
        marcado[inicio]=True

        while estructura:
            vo=estructura.popleft()
            orden.append(vo)
            vecinos = self.getVecinos(vo)

            for relacion in vecinos:
                destino = relacion.getDestino()
                peso = relacion.getPeso()

                if not marcado[destino]:
                    marcado[destino] = True
                    estructura.append(destino)

        return orden

    # recorrido en profundidad
    def dfs(self, inicio):
        orden = []

        marcado = [ False for i in range(len(self.grafo)) ]

        estructura = []
        estructura.append(inicio)

        marcado[inicio]=True

        while estructura:

            vo = estructura.pop()
            orden.append(vo)
            vecinos = self.getVecinos(vo)
            for relacion in vecinos :
                destino = relacion.getDestino()
                peso = relacion.getPeso()
                if not marcado[destino]:
                    marcado[destino] = True
                    estructura.append(destino)
        return orden


    def imprimirGrafo(self):
        matrizAdyasencia = [[0 for j in range(len(self.grafo))] for i in range(len(self.grafo))]

        for i in range(len(self.grafo)):
            for par in self.grafo[i] :
                matrizAdyasencia[i][par.getDestino()] = 1

        for vertices in matrizAdyasencia:
            for vertice in vertices:
                print(vertice, end=" ")
            print()



if __name__ == "__main__":
   
    #grafo de tamania 6 v
    grafo = Grafo(6)
    grafo.anadirArista(1, 2, 0)
    grafo.anadirArista(2, 1, 0)
    grafo.anadirArista(2, 3, 0)
    grafo.anadirArista(3, 2, 0)
    grafo.anadirArista(3, 4, 0)
    grafo.anadirArista(4, 3, 0)
    grafo.anadirArista(5, 0, 0)
    grafo.anadirArista(0, 5, 0)
    
    #grafo de tamanio 5 v para el ejemplo
    # grafo = Grafo(5)
    # grafo.anadirArista(0, 1, 0)
    # grafo.anadirArista(1, 0, 0)
    # grafo.anadirArista(0, 2, 0)  
    # grafo.anadirArista(2, 0, 0)
    # grafo.anadirArista(0, 3, 0)
    # grafo.anadirArista(3, 0, 0)
    # grafo.anadirArista(0, 4, 0)
    # grafo.anadirArista(4, 0, 0)
    # grafo.anadirArista(1, 2, 0)
    # grafo.anadirArista(2, 1, 0)
    # grafo.anadirArista(1, 3, 0)
    # grafo.anadirArista(3, 1, 0)
    # grafo.anadirArista(2, 3, 0)
    # grafo.anadirArista(3, 2, 0)
    # grafo.anadirArista(2, 4, 0)
    # grafo.anadirArista(4, 2, 0)
    # grafo.anadirArista(3, 4, 0)
    # grafo.anadirArista(4, 3, 0)

    # imprime grafo
    grafo.imprimirGrafo()
    print (grafo.getVecinos(1))
    #recorrido bfs
    print(grafo.bfs(1))
    #recorrido dfs
    print(grafo.dfs(1))