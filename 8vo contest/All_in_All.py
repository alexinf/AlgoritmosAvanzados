#!/usr/bin/python3
# coding: utf-8 

while(True):
    try:
        note = input()
    except EOFError:
        break
    palabra, codificado = note.split()
    cont = 0
    codificado = list(codificado)
    for x in palabra:
        while len(codificado) > 0:
            if x == codificado[0]:
                codificado.pop(0)
                cont +=1
                break
            else:
                codificado.pop(0)
    if(len(palabra) == cont):
        print ("Yes")
    else:
        print("No")



