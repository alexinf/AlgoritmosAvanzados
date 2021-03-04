def convertirNumbero(numero):
	b = str(numero)
	return list(b)
def volcarNumero(numero):
	b = []
	while numero > 0:
		d = int(numero%10)
		b.append(d)
		numero =int(numero/10)
	#print(b)
	salida = []
	#return [ b[x] for x in range(len(b)-1,-1,-1)]
	for x in range(len(b)):
		salida.append(b.pop())
	return salida

#[7,8,5,6]

a = volcarNumero(6587)
print(a)