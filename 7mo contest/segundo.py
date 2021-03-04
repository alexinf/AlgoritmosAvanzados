#!/usr/bin/python3
# coding: utf-8 

base = dict()
ord = dict()   

def make_set(v):
    base[v] = v
    ord[v] = 0

def find(v):
    if base[v] != v:
        base[v] = find(base[v])
    return base[v]

def union(u, v):
    v1 = find(u)
    v2 = find(v)
    if v1 != v2:
        if ord[v1] > ord[v2]:
            base[v2] = v1 
        else:
            base[v1] = v2
            if ord[v1] == ord[v2]: 
                ord[v2] += 1

def kruskal(graph):

    mst = set()
   
    for v in graph['vertices']:
        make_set(v)

    edges = list(graph['edges'])
    edges.sort()
    
    for e in edges:
        weight, u, v = e
        if find(u) != find(v):
            union(u, v)
            mst.add(e)
    return mst 



if __name__ == "__main__":

    while True:
        grafo = {}
        grafo ['vertices'] = []
        grafo ['edges'] = []
        costo_inicial = 0
        costo_optimo = 0
        linea = input()
        if linea == '0 0':
            break
        cruces, carreteras = map(int, linea.split())
        nodo = []
        for nodos in range(cruces):
            grafo['vertices'].append(str(nodos))

        for i in range(carreteras):
            x, y, z= list(input().split())
            costo_inicial +=int(z)
            grafo['edges'].append((int(z),str(x),str(y)))

        grafo['edges'] = set(grafo['edges'] )
        #print(grafo)

        camino_minio = kruskal(grafo)
        for x in camino_minio:
            costo_inicial -= int(x[0])
        print(costo_inicial)

