#Creador: Eduardo Javier Maldonado Acevedo

import os

Nodo = dict()
resultado = {}
conjuntos = []

def Make_set(vertice):
    Nodo[vertice] = vertice

def Find_set(vertice):
    if Nodo[vertice] != vertice:
        Nodo[vertice] = Find_set(Nodo[vertice])
    return Nodo[vertice]

def Union(u, v, Ordenada):
    '''print "Conjuntos separados:",u,v
    if u not in conjuntos:
        print u,"No existe en conjuntos"
        conjuntos.append(u)
    else:
        print u,"Si existe en conjuntos"
    if v not in conjuntos:
        print v,"No existe en conjuntos"
        conjuntos.append(v)
    else:
        print v,"Si existe en conjuntos"
    print "Conjuntos unidos:",conjuntos'''
    Dato1 = Find_set(u)
    Dato2 = Find_set(v)
    if Dato1 != Dato2:
        for Dato in Ordenada:
            Nodo[Dato1] = Dato2

def Kruskal(grafo):
    resultante = []
    cont = 0
    for vertice in grafo['A']:
        Make_set(vertice)

    Ordenada = list(grafo['B'])
    Ordenada.sort()
    Ordenada = [(a,b,c) for c,a,b in Ordenada]
    Ordenada = [(c,a,b) for a,b,c in Ordenada]
    for Dato in Ordenada:
        peso, u, v = Dato
        if Find_set(u) != Find_set(v):
            resultante.append(Dato)
            resultante = [(a,b,c) for c,a,b in resultante]
            resultante = [(c,a,b) for a,b,c in resultante]
            cont+=1
            Union(u, v, Ordenada)

    return resultante

grafo = {
        'A': ['a','b','c','d','e','f','g','h'],
        'B': [(3, 'a', 'b'),
              (1, 'a', 'c'),
              (5, 'b', 'g'),
              (1, 'b', 'd'),
              (2, 'd', 'c'),
              (4, 'd', 'e'),
              (5,'c', 'f'),
              (3, 'f', 'h'),
              (2, 'f', 'd'),
              (1, 'h', 'e'),
              (2, 'g', 'e'),
            ]
        }
resultante = Kruskal(grafo)
print (resultante)