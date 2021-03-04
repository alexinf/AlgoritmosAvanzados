#!/usr/bin/python
# coding: utf-8

import math


def dist(*b):
 return math.sqrt((b[0] - b[2])**2 + (b[1] - b[3])**2)
 
def area(*b):
 x = dist(b[0], b[1], b[4], b[5])
 y = dist(b[0], b[1], b[2], b[3])
 z = dist(b[2], b[3], b[4], b[5])
 s = (x + y + z) / 2
 return math.sqrt(s * (s-x) * (s-y) * (s-z))

if name == "__main__": 

    a = []
    while True:
        n = input()
        if n == "*":
            break
        
        n = n.split()
        m = [n[0]]
        m += list(map(float, n[1:]))
        a.append(m) 

    c = 1

    while True:
        x, y = list(map(float, input().split()))
        if x == 9999.9 and y == 9999.9:
            break
        
        check = 1
        for i in range(len(a)):
            if a[i][0] == "r":
                if a[i][1] < x and x < a[i][3] and a[i][2] > y and y > a[i][4]:
                    print("Point {} is contained in figure {}".format(c, i+1))
                    check = 0
            elif a[i][0] == "c":
                if a[i][3] > dist(a[i][1], a[i][2], x, y):
                    print("Point {} is contained in figure {}".format(c, i+1))
                    check = 0
            else:
                allArea = area(a[i][1], a[i][2], a[i][3], a[i][4], a[i][5], a[i][6])
                areaA = area(x, y, a[i][1], a[i][2], a[i][5], a[i][6])
                areaB = area(x, y, a[i][1], a[i][2], a[i][3], a[i][4])
                areaC = area(x, y, a[i][3], a[i][4], a[i][5], a[i][6])
                
                if areaA == 0 or areaB == 0 or areaC == 0:
                    continue
                if abs(allArea - areaA - areaB - areaC) < 0.001:
                    print("Point {} is contained in figure {}".format(c, i+1))
                    check = 0
                
        
        if check:
            print("Point {} is not contained in any figure".format(c))

        
        c += 1