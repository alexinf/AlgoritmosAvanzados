import sys
import numpy as np
import matplotlib.pyplot as plt

# Function to know if we have a CCW turn
def RightTurn(p1, p2, p3):
	if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
		return False
	return True
	
# Main algorithm:
def GrahamScan(P):
	#P.sort(key=lambda coche : coche[1])			# Sort the set of points
	P.sort()
	print(P)
	L_upper = [P[0], P[1]]		# Initialize upper part
	# Compute the upper part of the hull
	for i in range(2,len(P)):
		L_upper.append(P[i])
		while len(L_upper) > 2 and not RightTurn(L_upper[-1],L_upper[-2],L_upper[-3]):
			del L_upper[-2]
	L_lower = [P[-1], P[-2]]	# Initialize the lower part
	# Compute the lower part of the hull
	for i in range(len(P)-3,-1,-1):
		L_lower.append(P[i])
		while len(L_lower) > 2 and not RightTurn(L_lower[-1],L_lower[-2],L_lower[-3]):
			del L_lower[-2]
	del L_lower[0]
	del L_lower[-1]
	L = L_upper + L_lower		# Build the full hull
	return np.array(L)

def main():
	try:
		N = int(sys.argv[1])
	except:
		N = int(input("Introduce N: "))
	# By default we build a random set of N points with coordinates in [0,300)x[0,300):
	#P = [(np.random.randint(0,300),np.random.randint(0,300)) for i in range(N)]
	#P = [(28, 193), (3, 289), (233, 114), (22, 157), (234, 169), (110, 233), (200, 52), (221, 233), (147, 215), (197, 29), (194, 14), (6, 115)]
	#print("puntos:" , P)
	P = [(0, 9),
 		 (2, 14),
 		 (7, 15),
 		 (12, 14),
 		 (15, 9),
 		 (14, 4),
 		 (10, 1),
 		 (5, 1),
 		 (1, 4),
 		 (1, 6),
 		 (3, 12),
 		 (9, 14),
 		 (12, 12),
 		 (14, 8),
 		 (12, 4),
 		 (7, 2),
 		 (3, 4),
 		 (3, 8),
 		 (3, 10),
 		 (5, 12),
 		 (9, 12),
 		 (11, 11),
 		 (12, 6),
 		 (9, 4),
 		 (5 ,4),
 		 (5, 8),
 		 (9 ,11),
 		 (11, 9),
 		 (10, 6),
 		 (7, 5),
 		 (6 ,6),
 		 (6, 7),
 		 (7 ,8),
 		 (10, 7),
 		 (9 ,6),
 		 (5, 5)]
	L = GrahamScan(P)
	print(L)
	P = np.array(P)
	
	# Plot the computed Convex Hull:
	plt.figure()
	plt.plot(L[:,0],L[:,1], 'b-', picker=5)
	plt.plot([L[-1,0],L[0,0]],[L[-1,1],L[0,1]], 'b-', picker=5)
	plt.plot(P[:,0],P[:,1],".r")
	plt.axis('off')
	plt.show()

if __name__ == '__main__':
	main()