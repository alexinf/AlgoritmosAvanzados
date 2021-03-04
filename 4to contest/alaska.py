#!/usr/bin/python3
# coding: utf-8 

while True:
    n = int(input())
    if n == 0:
        break
    charge = []
    for x in range(n):
        y = int(input())
        charge.append(y)
    charge.sort()
    possibility= True
    if (1422 - charge[n-1]) > 100:
        possibility = False
    else:
        for x in range(1,n):
            if (charge[x]-charge[x-1] > 200):
                possibility = False
                break
    if (possibility):
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

    