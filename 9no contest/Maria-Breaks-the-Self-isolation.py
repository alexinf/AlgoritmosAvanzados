#!/usr/bin/python3
# coding: utf-8 

casos = int(input())
for x in range(casos):
    numV = int(input())
    vector  = list(map(int, input().split()))
    vector.sort()
    #print(vector)
    ab = 1
    antAb = -1
    for y in range(numV):
        if ab >= vector[y]:
            antAb = y
        ab +=1
        #print (antAb)
    print(antAb+2)
