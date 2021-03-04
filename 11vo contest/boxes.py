# import sys
# import numpy as np
# INF = 1 << 31
# MAXB = 3005


# def solve(par):
#     N, cajas = par
#     memo = np.zeros((N, MAXB), dtype=int)
#     # print(memo)
#     #memo = [[0 for x in range(N)] for y in range(MAXB)] 
#     #memo = [[0]*MAXB for i in range(N)]
#     print(memo)
#     def cajasM(numLi, cargaMax):
#         if memo[numLi, cargaMax]:
#             return memo[numLi, cargaMax]
#         if not cargaMax:
#             return 0
#         cajasMax = 1
#         for i in range(numLi + 1, N):
#             if cajas[i][0] <= cargaMax:
#                 m1 = cajasM(i, cargaMax - cajas[i][0]) + 1
#                 cajasMax = max(cajasMax, m1)
#         memo[numLi, cargaMax] = cajasMax
#         return cajasMax
#     return max(cajasM(i, cajas[i][1]) for i in range(N))

# while True:
#     N = int(input())
#     if N == 0:
#         break
#     cajas = []
#     for i in range(N):
#         a,b = map(int, input().split())
#         cajas.append([a,b])
#         #print(cajas)
#     print(solve((N, cajas)))

#!/usr/bin/python3
# coding: utf-8 
from sys import stdin

MAXB = 3005

def solucion(par):
    N, cajas = par
    mem = [[0]*MAXB for i in range(N)]
    #print(memo)
    def cajasM(numLi, cargaMax):
        if mem[numLi][cargaMax]:
            return mem[numLi][cargaMax]
        if not cargaMax:
            return 0
        cajasMax = 1
        for i in range(numLi + 1, N):
            if cajas[i][0] <= cargaMax:
                m1 = cajasM(i, cargaMax - cajas[i][0]) + 1
                cajasMax = max(cajasMax, m1)
        mem[numLi][cargaMax] = cajasMax
        return cajasMax
    return max(cajasM(i, cajas[i][1]) for i in range(N))

while True:
    N = int(stdin.readline().strip())
    if N == 0:
        break
    cajas = []
    for i in range(N):
        a,b = map(int, stdin.readline().split())
        cajas.append([a,b])
        #print(cajas)
    print(solucion((N, cajas)))