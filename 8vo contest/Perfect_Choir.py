#!/usr/bin/python3
# coding: utf-8 

while(True):
    try:
        miembros = int(input())
    except EOFError:
        break
    notas = list(map(int,input().split()))
    total_notas = sum(notas)
    comp_min = 0
    if total_notas%miembros > 0:
        print("-1")
    else:
        for x in notas: 
            comp_min += abs((total_notas/miembros)-x)
        print(int(1+(comp_min/2)))