#!/usr/bin/python3
# coding: utf-8 
import operator

s = int(input())
for x in range(s):
    num_bat = int(input())
    voltaje = int(input())
    baterias = list(map(int, input().split()))
    dicc_bat  = {}
    robots = []
    ind = 1
    for x in baterias:
        dicc_bat [ind] = x
        ind +=1
        
    dicc_bat_ordenado = sorted(dicc_bat.items(), key=operator.itemgetter(1), reverse = True)
    izq  = 0
    der = len(dicc_bat_ordenado) -1

    while izq < len(dicc_bat_ordenado) -1:
        bat_izq = dicc_bat_ordenado[izq]
        bat_der = dicc_bat_ordenado[der]
        if (bat_izq[1]+bat_der[1]) >= voltaje and not bat_izq[0] in robots and not bat_der[0] in robots and bat_izq[0] != bat_der[0]:
            if bat_izq[1] == bat_der[1]:
                robots.append(bat_izq[0])
                robots.append(bat_der[0])
            else: 
                robots.append(bat_der[0])
                robots.append(bat_izq[0])
            izq +=1
            der =len(dicc_bat_ordenado) -1
        else:
            der -=1
            if der == izq:
                der = len(dicc_bat_ordenado) -1
                izq +=1
    #print(robots)
    res = [str(x) for x in robots]
    print(str(int(len(robots)/2)) + ": " +' '.join(res))