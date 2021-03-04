#!/usr/bin/python3
# coding: utf-8 

import operator

bb = 0

while True:
    
    try:
        string = input()
    except EOFError:
        break

    if bb > 0:
        print()

    asciiCont = {}
    maxC = 0
    for x in string:
        asciiV = ord(x)
        if asciiV in asciiCont:
            asciiCont[asciiV] = asciiCont.get(asciiV)+1
        else:
            asciiCont[asciiV] = 1
        maxC +=1
    #a = list(asciiCont.keys())[list(asciiCont.values()).index(3)]
    #print(a)
    result = sorted(asciiCont.items(), key=operator.itemgetter(0), reverse = True)  
    bb = 1

    for x in range(1,maxC+1):
        for y in result:
            if x == y[1]:
                print(str(y[0])+ ' '+ str(y[1]))
