import math

esp = 1e-6
while True:
	try:
		l, w = map(float, input().split())
	except EOFError:
		break
	x = (l + w - math.sqrt((l*l)+(w*w)-(w*l)))/6 + esp
	if l < w:
		y = l/2.0 + esp
	else:
		y = (w/2.0) + esp
	print("{:.3f} 0.000 {:.3f}".format(x, y))