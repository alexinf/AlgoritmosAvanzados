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
    #print(dicc_bat_ordenado)

    for indice, batt in dicc_bat_ordenado:
        for indice2,batt2 in dicc_bat_ordenado[::-1]:
            if (batt+batt2) >= voltaje and not indice2 in robots and not indice in robots and indice != indice2:
                if int(batt) == int(batt2):
                    #print("--")
                    robots.append(indice)
                    robots.append(indice2)
                else: 
                    robots.append(indice2)
                    robots.append(indice)
    res = [str(x) for x in robots]
    print(str(int(len(robots)/2)) + ": " +' '.join(res))
    
    # num_batt = []
    # for x in range(0,len(robots),2):
    #     if dicc_bat[robots[x]] > dicc_bat[robots[x+1]]:
    #         num_batt.append(str(robots[x+1]))
    #         num_batt.append(str(robots[x]))
    #     else:
    #         num_batt.append(str(robots[x]))
    #         num_batt.append(str(robots[x+1]))
    # print(str(int(len(num_batt)/2)) + ": " +" ".join(num_batt))    