#!/usr/bin/python
# coding: utf-8
#import operator

casos = int(input())

for x in range(casos):
	contactos = []
	numCont = int(input())
	for y in range(1,numCont+1):
		nom, tel = input().split()
		contactos.append((tel,y))
	numEsp = input()
	resp = []
	for tel in contactos:
		if tel[0].startswith(numEsp):
			resp.append(tel)
	resp = sorted(resp)
	if resp == []:
		print("Activado")
	else:
		for x in resp:
			print(x[1], end= " ")
		print()


