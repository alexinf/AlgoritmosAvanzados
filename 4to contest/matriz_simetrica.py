#!/usr/bin/python3
# coding: utf-8 

def Symmetric(matrix, n):
    resp = 'Symmetric.'
    for x in range(n):
        for y in range(n-x):
            if (matrix[x][y] < 0 or matrix[x][y] != matrix[n-1-x][n-1-y]):
                resp = 'Non-symmetric.'
                break
    return resp

line = int(input())
result = []
cont = 1
for x in range(line):
    n = list(input().split())
    matrix = []
    for x in range(int(n[2])):
        row = list(map(int, input().split()))
        matrix.append(row)
    result.append(Symmetric(matrix, int(n[2])))
    print ('Test #'+ str(cont) +': '+ Symmetric(matrix, int(n[2])))
    cont += 1