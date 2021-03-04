#!/usr/bin/python
# coding: utf-8


def alfabeto(peso, rep, *args):
    pools = [tuple(pool) for pool in args] * rep
    #print(pools)
    cont = 0
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        #yield tuple(prod)
        if sum(prod) == peso:
            cont +=1
    return cont


while(True):
    try:
        numC, peso =map(int, input().split())
    except EOFError:
        break
    cont = 0    
    if (numC%2 == 0) and (peso %2 ==0):
        resp = alfabeto(int(peso/2),int(numC/2),[0, 1, 2, 3, 4, 5])
        print(resp*resp)
    else:
        print(0)  
