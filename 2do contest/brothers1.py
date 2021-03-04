#!/usr/bin/python3
# coding: utf-8 

while True:
    movimiento = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    line = input()
    
    hermanos, fila, columna, peleas = map(int, line.split())
    reyno = []

    if not hermanos:
        break

    for x in range(fila):
        f = list(map(int, input().split()))
        reyno.append(f)
    atacar = []
    for x in range(hermanos-1):
        atacar.append(x+1)
    atacar.append(0)

    while peleas > 0:
        temp = [x[:] for x in reyno]
        for i in range(fila):
            for j in range(columna):
                for k in range(4):
                    y = i + movimiento[k][0]
                    x = j + movimiento[k][1]
                    if y > -1 and y < fila and x > -1 and x < columna and atacar[reyno[i][j]] == reyno[y][x]:
                        temp[y][x] = reyno[i][j]
        peleas -= 1
        reyno = temp

    for x in reyno:
        print( " ".join(map(str, x)) )





