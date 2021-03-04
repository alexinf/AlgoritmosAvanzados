#!/usr/bin/python3
# coding: utf-8 

def rotar():
	global matriz
	aux = [[ valor for valor in x ]for x in matriz]
	n = len(matriz)
	for i in range(n):
		for j in range(n):
			matriz[i][j] = aux[n-j-1][i]


def reflexion():
	global matriz
	aux = [[ valor for valor in x ]for x in matriz]
	n = len(matriz)
	for i in range(n):
		for j in range(n):
			matriz[i][j] = aux[n-i-1][j]


def compara( matrizA, matrizB ):
	bandera = True
	for i in range(len(matrizA)):
		for j in range(len(matrizA)):
			if matrizA[i][j] != matrizB[i][j]:
				bandera = False
				break
		if(not bandera):
			break	
	return bandera

numRegistro = 0
while True:
	numRegistro+=1
	try:
		n = input()
	except EOFError:
		break
	n = int(n)
	matriz=[]
	matrizB=[]
	for i in range(n):
		x, y = input().split()
		matriz.append(list(x))
		matrizB.append(list(y))

	if compara(matriz, matrizB):
		print('Pattern '+ str(numRegistro) +' was preserved.')
		continue

	rotar()
	if compara(matriz, matrizB):
		print('Pattern ' + str(numRegistro) +' was rotated 90 degrees.')
		continue
	
	rotar()
	if compara(matriz, matrizB):
		print('Pattern ' + str(numRegistro) +' was rotated 180 degrees.')
		continue
	
	rotar()
	if compara(matriz, matrizB):
		print('Pattern ' + str(numRegistro) +' was rotated 270 degrees.')
		continue
	
	rotar()
	reflexion()
	if compara(matriz, matrizB):
		print('Pattern ' + str(numRegistro) +' was reflected vertically.')
		continue
	
	rotar()
	if compara(matriz, matrizB):
		print('Pattern ' + str(numRegistro) +' was reflected vertically and rotated 90 degrees.')
		continue
	
	rotar()
	if compara(matriz, matrizB):
		print('Pattern ' + str(numRegistro) +' was reflected vertically and rotated 180 degrees.')
		continue
	
	rotar()
	if compara(matriz, matrizB):
		print('Pattern ' + str(numRegistro) +' was reflected vertically and rotated 270 degrees.')
		continue
	print('Pattern ' + str(numRegistro) +' was improperly transformed.')