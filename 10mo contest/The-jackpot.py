#!/usr/bin/python3
# coding: utf-8 

while True:
	jugadas = []
	tam = 0
	n = int(input())
	if n == 0:
		break

	while (tam < n):
		jugada  = list(map(int, input().split()))
		jugadas = jugadas + jugada
		tam = len(jugadas)
	tam = 0
	maximo = 0
	aux = 0
	for x in range(n):
		aux += jugadas[x]
		if (aux > maximo):
			maximo = aux
		if (aux < 0):
			aux = 0
	if (maximo > 0):
		print ('The maximum winning streak is ' + str(maximo)+ '.')
	else:
		print ('Losing streak.')


