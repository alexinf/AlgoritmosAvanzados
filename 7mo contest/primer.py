#!/usr/bin/python3
# coding: utf-8 

from sys import stdin

class Grafo:
    def __init__(self):
        self.vertices = []
        self.matriz = [[None]*0 for i in range(0)]

    @staticmethod
    def contenido_en(lista, k):
        if lista.count(k) == 0:
            return False
        return True

    def esta_en_vertices(self, v):
        if self.vertices.count(v) == 0:
            return False
        return True

    def agregar_vertices(self, v):
        if self.esta_en_vertices(v):
            return False

        self.vertices.append(v)
        filas = columnas = len(self.matriz)
        matriz_aux = [[None] * (filas+1) for i in range(columnas+1)]

        for f in range(filas):
            for c in range(columnas):
                matriz_aux[f][c] = self.matriz[f][c]

        self.matriz = matriz_aux
        return True

    def agregar_arista(self, inicio, fin, dirijida):
        if not(self.esta_en_vertices(inicio)) or not(self.esta_en_vertices(fin)):
            return False
        
        self.matriz[self.vertices.index(inicio)][self.vertices.index(fin)] = 1

        if not dirijida:
            self.matriz[self.vertices.index(fin)][self.vertices.index(inicio)] = 1
        return True

    def obtener_sucesores(self, v):
        pos_vertice = self.vertices.index(v)

        list_sucesores = []

        for i in range(len(self.matriz)):
            if self.matriz[pos_vertice][i] is not None:
                list_sucesores.append(self.vertices[i])

        return list_sucesores


if __name__ == "__main__":

    casos = int(stdin.readline().strip())
    for x in range(casos):
        grafo = Grafo()
        r = stdin.readline().strip()
        p_aspersor = list(set(r))
        
        for nodos in p_aspersor:
            grafo.agregar_vertices(nodos)
        aristas = list(r)  
        recorrido = 0  

        while aristas:
            
            if not aristas[recorrido] == aristas [recorrido+1]:
                grafo.agregar_arista(aristas[recorrido],aristas[recorrido+1],False)
                #print(aristas[recorrido] + aristas[recorrido+1])
                recorrido += 1
            else:
                if not recorrido < len(aristas)-1:
                    break
                else:
                    aristas.pop(recorrido)
                    aristas.pop(recorrido)
                    recorrido -=1
        print("Case " +str(x+1))
        for nodo in sorted(p_aspersor):
            print(nodo + ' = ' + str(len(grafo.obtener_sucesores(nodo))))
