#!/usr/bin/python3
# coding: utf-8 

from statistics import mode

class DisjointUnionSets: 
    def __init__(self, n): 
        self.rank = [0] * n 
        self.parent = [0] * n 
        self.n = n 
        self.makeSet() 

    def makeSet(self): 
        for i in range(self.n): 
            self.parent[i] = i 

    def find(self, x): 
        if (self.parent[x] != x): 
            self.parent[x] = self.find(self.parent[x]) 
            return self.parent[x]
        return x 

    def Union(self, x, y): 
        
        xRoot = self.find(x) 
        yRoot = self.find(y) 

        if xRoot == yRoot: 
            return
 
        if self.rank[xRoot] < self.rank[yRoot]: 
            self.parent[xRoot] = yRoot 
 
        elif self.rank[yRoot] < self.rank[xRoot]: 
            self.parent[yRoot] = xRoot 

        else: 
            self.parent[yRoot] = xRoot 
            self.rank[xRoot] = self.rank[xRoot] + 1

def tamZonas(a , x, y): 
    n = int(x) 
    m = int(y) 

    dus = DisjointUnionSets(n * m) 

    for j in range(0, n): 
        for k in range(0, m): 

            if a[j][k] == 0: 
                continue

            if j + 1 < n and a[j + 1][k] == 1: 
                dus.Union(j * (m) + k, 
                        (j + 1) * (m) + k) 
            if j - 1 >= 0 and a[j - 1][k] == 1: 
                dus.Union(j * (m) + k, 
                        (j - 1) * (m) + k) 
            if k + 1 < m and a[j][k + 1] == 1: 
                dus.Union(j * (m) + k, 
                        (j) * (m) + k + 1) 
            if k - 1 >= 0 and a[j][k - 1] == 1: 
                dus.Union(j * (m) + k, 
                        (j) * (m) + k - 1) 
            if (j + 1 < n and k + 1 < m and
                    a[j + 1][k + 1] == 1): 
                dus.Union(j * (m) + k, (j + 1) *
                            (m) + k + 1) 
            if (j + 1 < n and k - 1 >= 0 and
                    a[j + 1][k - 1] == 1): 
                dus.Union(j * m + k, (j + 1) *
                            (m) + k - 1) 
            if (j - 1 >= 0 and k + 1 < m and
                    a[j - 1][k + 1] == 1): 
                dus.Union(j * m + k, (j - 1) *
                            m + k + 1) 
            if (j - 1 >= 0 and k - 1 >= 0 and
                    a[j - 1][k - 1] == 1): 
                dus.Union(j * m + k, (j - 1) *
                            m + k - 1) 

    c = [0] * (n * m) 
    for j in range(n): 
        for k in range(m): 
            if a[j][k] == 1: 
                x = dus.find(j * m + k) 
                if c[x] == 0: 
                    c[x] += 1
                else: 
                    c[x] += 1
    lista = dus.parent
    tzona = lista.count(mode(lista))
    return tzona

while True:
    resp = []
    try:
        x, y = input().split()
    except EOFError:
        break
    matriz = []
    for i in range(int(x)):
        fila = list(map(int, input()))
        matriz.append(fila)

    resp.append(str(tamZonas(matriz, x, y)))
    vr = int(input())

    for j in range(vr):
        calles = list(map(int,input().split()))
        matriz[calles[0]-1][calles[1]-1] = 1
        resp.append(str(tamZonas(matriz, x, y)))
    print(' '.join(resp))
    