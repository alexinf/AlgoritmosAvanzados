#!/usr/bin/python
# coding: utf-8

def resolv(ax, ay, N, x, y):
    if ( (ax%N) == 1 or (ay%N) ==  1 ):
        return False
    ax /= N
    ay /= N
    for i in range(N):
        xb = 2 * int(ax) - x[i]
        yb = 2 * int(ay) - y[i]
        bb = False
        for j in range(N):
            if (xb == x[j] and yb == y[j]):
                bb = True
                break
        if bb == False:
            return False
    return True


cases = int(input())
x = [0]*10005
y = [0]*10005
for i in range(cases):
    N = int(input())
    ax = 0
    ay = 0
    for j in range(N):
        cx, cy = map(int, input().split())
        x[j] = cx
        y[j] = cy
        ax += cx
        ay +=cy
    print(x,y)
    if ((N == 1) or resolv(ax, ay, N, x , y)):
        print("yes")
    else:
        print("no")