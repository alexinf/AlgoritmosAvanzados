# Author: Rodolfo Ferro 
# Mail: ferro@cimat.mx
# Script: Compute the Convex Hull of a set of points using the Graham Scan

import sys
import numpy as np
import matplotlib.pyplot as plt

# Function to know if we have a CCW turn
def CCW(p1, p2, p3):
	if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
		return True
	return False

# Main function:
def jarvis_march(points):
    # find the leftmost point
    a =  min(points, key = lambda point: point.x)
    index = points.index(a)
    
    # selection sort
    l = index
    result = []
    result.append(a)
    while (True):
        q = (l + 1) % len(points)
        for i in range(len(points)):
            if i == l:
                continue
            d = direction(points[l], points[i], points[q])
            if d > 0 or (d == 0 and distance_sq(points[i], points[l]) > distance_sq(points[q], points[l])):
                q = i
        l = q
        if l == index:
            break
        result.append(points[q])

    return result

def main():
	try:
		N = int(sys.argv[1])
	except:
		N = int(input("Introduce N: "))
	
	# By default we build a random set of N points with coordinates in [0,300)x[0,300):
	P = np.array([(np.random.randint(0,300),np.random.randint(0,300)) for i in range(N)])
	L = jarvis_march(P)
	print(L)

if __name__ == '__main__':
  main()