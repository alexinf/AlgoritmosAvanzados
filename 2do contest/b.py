#!/usr/bin/python3
# coding: utf-8 

while True:

    tamanio = int(input())
    if tamanio == 0:
        break
    autos = [ -1 for i in range(tamanio)]
    bandera = False 

    for i in range(tamanio):
        C, P = map(int, input().split(' '))
        
        if (i+P < 0 or i+P >= tamanio):
            bandera = True

        if (not bandera and autos[i+P] != -1):
            bandera = True
        
        if (not bandera):
            autos[i+P] = C
    
    resultado = -1 if bandera else " ".join(map(str, autos))
    print(resultado)