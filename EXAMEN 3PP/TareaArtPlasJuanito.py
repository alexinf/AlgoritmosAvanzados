import sys

def RightTurn(p1, p2, p3):
	if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
		return False
	return True
	
def GrahamScan(P):
	P.sort()
	puntSup = [P[0], P[1]]
	for i in range(2,len(P)):
		puntSup.append(P[i])
		while len(puntSup) > 2 and not RightTurn(puntSup[-1],puntSup[-2],puntSup[-3]):
			del puntSup[-2]
	puntInf = [P[-1], P[-2]]	
	for i in range(len(P)-3,-1,-1):
		puntInf.append(P[i])
		while len(puntInf) > 2 and not RightTurn(puntInf[-1],puntInf[-2],puntInf[-3]):
			del puntInf[-2]
	del puntInf[0]
	del puntInf[-1]
	grafRes = puntSup + puntInf
	return grafRes


N = int(input())
P = []
for x in range(1,N+1):
	C = int(input())
	if C < 3:
		continue
	for z in range (C):
		coord = tuple(map(int, input().split(" ")))
		P.append(coord)
	result = []
	while(True):
		if(len(P) == 0):
			break
		elif(len(P) == 1):
			P.pop()
			result.append(str(1))
		else:
			L = GrahamScan(P)
			result.append(str(len(L)))
			for y in L:
				P.remove(y)

	resp = "Caso {0}: {1}".format(x, " ".join(result))
	print(resp) 
