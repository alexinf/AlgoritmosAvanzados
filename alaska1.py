#!/usr/bin/python3
# coding: utf-8


while True:
    n = int(input())
    if n == 0:
        break
    station = []
    for i in range(n):
        a = int(input())
        station.append(a)
    station.sort()
    flag = True
    total = 0
    
    for i in range(n-1):
        if (station[i+1] - station[i]) > 200:
            flag = False
            break
        total = total + (station[i+1] - station[i])
    
    if (station[0] - 0) > 200:
        flag = False
    elif station[0] != 0:
        total = total + (station[0] - 0)
    
    if (1422 - station[n-1]) > 100:
        flag = False
    elif station[n-1] != 1422:
        total = total + (1422 - station[n-1])	
    
    if total != 1422:
        flag = False
    
    if flag == True:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
