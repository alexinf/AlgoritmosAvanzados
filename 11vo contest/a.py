#!/usr/bin/python3
# coding: utf-8 

casos = int(input())

for c in range(casos):
	compras = [0]*31
	numC = int(input())
	for x in range(numC):
		a, b = map(int, input().split())
		for y in range(30,b-1,-1):
			if(compras[y]<compras[y-b]+a):
				compras[y]= compras[y-b]+a

	numP = int(input())
	resp = 0
	for x in range(numP):
		pMax = int(input())
		resp += compras[pMax]
	print(resp) 









