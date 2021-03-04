#!/usr/bin/python3
# coding: utf-8 

entrada = input()
if entrada == "0":
	n = int(entrada)
else:
	entrada = entrada.split(' ')
	n = int(entrada[0])
	cadena = entrada[1]
while n!=0:
	
	nCad = len(cadena)
	salida = ""
	div = int(nCad/n)
	for i in range(0,nCad, div):
		salida += cadena[i: i+div][::-1]

	print(salida)
	entrada = input()
	if entrada == "0":
		n = int(entrada)
	else:
		entrada = entrada.split(' ')
		n = int(entrada[0])
		cadena = entrada[1]
