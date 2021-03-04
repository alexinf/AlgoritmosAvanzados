#formula para r de una circunferecia dentro un triangulo a + b = c + 2r
# 1.00 3.00 5.00 7.00 7.00 0.00 4.09 3.50
# 2.00 4.00 5.00 9.00 7.00 3.00 4.57 5.13
# (2.00, 4.00)
# (5.00, 9.00)
# (7.00, 3.00)
# (4.57, 5.13)
#float("{0:.2f}".format(x))
import math

def RotarP(Origin, point, angle):
    ox, oy = Origin
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    aux = str(qx).split('.')
    auy = str(qy).split('.')
    return float(".".join([aux[0], aux[1][0:2]])), float(".".join([auy[0], auy[1][0:2]]))

def intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    aux = str(x).split('.')
    auy = str(y).split('.')
    return float(".".join([aux[0], aux[1][0:2]])), float(".".join([auy[0], auy[1][0:2]]))

def AreaT(X,Y,Z):
	a1 = (Y[1]-X[1])**2 + (Y[0]-X[0])**2
	a = math.sqrt(a1)
	b1 = (Z[1]-Y[1])**2 + (Z[0]-Y[0])**2
	b = math.sqrt(b1)
	c1 = (Z[1]-X[1])**2 + (Z[0]-X[0])**2
	c = math.sqrt(c1)
	p = (a+b+c)/2.0
	A1 = p*(p-a)*(p-b)*(p-c)
	A = math.sqrt(A1)
	return float("{0:.2f}".format(A))


result = 0
A = (1.00, 3.00)
B = (5.00, 7.00)
C = (7.00, 0.00)
r = (4.09, 3.50)
# A = (2.00, 4.00)
# B = (5.00, 9.00)
# C = (7.00, 3.00)
# r = (4.57, 5.13)
A1 =RotarP(r, A, math.radians(180))
B1 =RotarP(r, B, math.radians(180))
C1 =RotarP(r, C, math.radians(180))
print("A1 ",A1)
print("B1 ",B1)
print("C1 ",C1)

T1A = intersection((A1,C1),(B,C))
T1B = intersection((A1,C1),(B,A))
T1C = B
print("T1A",T1A)
result += AreaT(T1A,T1B,T1C)
#print(result)

###############################################

T2A = intersection((B1,C1),(A,B))
T2B = intersection((B1,C1),(A,C))
T2C = A
print("T2A",T2A)
result += AreaT(T2A,T2B,T2C)
#print(result)

###############################################
T3A = intersection((B1,A1),(C,B))
T3B = intersection((B1,A1),(C,A))
T3C = C
result += AreaT(T3A,T3B,T3C)
print(result)

print(AreaT(A,B,C))