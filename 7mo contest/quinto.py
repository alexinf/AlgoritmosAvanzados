#!/usr/bin/python3
# coding: utf-8 

from sys import stdin

base = dict()
ord = dict()
    
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

    def agregar_arista(self, inicio, fin,costo, dirijida):
        if not(self.esta_en_vertices(inicio)) or not(self.esta_en_vertices(fin)):
            return False
        
        self.matriz[self.vertices.index(inicio)][self.vertices.index(fin)] = costo

        if not dirijida:
            self.matriz[self.vertices.index(fin)][self.vertices.index(inicio)] = costo
        return True

    def obtener_sucesores(self, v):
        pos_vertice = self.vertices.index(v)

        list_sucesores = []

        for i in range(len(self.matriz)):
            if self.matriz[pos_vertice][i] is not None:
                list_sucesores.append(self.vertices[i])

        return list_sucesores

    def make_set(self, v):
        base[v] = v
        ord[v] = 0
    
    # Implementación de la función de búsqueda 
    # de manera recursiva
    def find(self, v):
        if base[v] != v:
            base[v] = self.find(base[v])
        return base[v]
    
    # Implementación de la unión de conjuntos
    def union(self, u, v):
        v1 = self.find(u)
        v2 = self.find(v)
        if v1 != v2:
            if ord[v1] > ord[v2]:
                base[v2] = v1 
            else:
                base[v1] = v2
                if ord[v1] == ord[v2]: 
                    ord[v2] += 1
    
    # Función principal del algoritmo Kruskal
    def kruskal(self,nodo):
    
        # A = {conjunto vacío}
        mst = set()
       
        # Para todo vértice v en G.V
        for v in self.vertices:
            self.make_set(v)
        print ("Sub gráficos creados:")
        print (base)
    
        # Ordena la lista G.E en forma no decendente por su peso w
        # En este caso usamos el ordenador dentro de python
        edges = list(self.matriz)
        edges.sort()
        
        print ("Aristas ordenadas:")
        print (edges)
    
        # Para toda arista(u,v) en G.E
        for e in edges:
            print("aqui ", e)
            u, v, weight = e
            # Si encontrar-conjunto(u) != encontrar-conjunto(v)
            if self.find(u) != self.find(v):
                # A = A union (u,v)
                self.union(u, v)
                # Union(u,v)
                mst.add(e)
        return mst 

if __name__ == "__main__":
    
    while True:
        grafo = Grafo()
        linea = input()
        if linea == '0 0':
            break
        cruces, carreteras = map(int, linea.split())
        nodo = []
        for nodos in range(cruces):
            grafo.agregar_vertices(nodos)
            nodo.append(str(nodos))
 
        for i in range(carreteras):
            x, y, z= list(input().split())
            grafo.agregar_arista(str(x),str(y),int(z),False)

        print(grafo.kruskal(nodo))






    
