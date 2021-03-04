#!/usr/bin/python3
# coding: utf-8 

inicioText = 0
while True:
	try :
		text = input()
	except EOFError:
		break	

	cadena = []
	for x in text:
		if x == "\"":
			if inicioText == 0:
				cadena.append("``")
				inicioText = 1
			else:
				cadena.append("''")
				inicioText = 0
		else:
			cadena.append(x)
	print("".join(cadena))