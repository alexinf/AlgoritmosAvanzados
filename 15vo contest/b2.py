#!/usr/bin/python
# coding: utf-8

def resolv(ax, ay, N, pair):
    if ( (ax%N) == 1 or (ay%N) ==  1 ):
        return False
    ax /= N
    ay /= N
    for i in range(N):
        xb = 2 * int(ax) - pair[i][0]
        yb = 2 * int(ay) - pair[i][1]
        bb = False
        for j in range(N):
            if (xb == pair[j][0] and yb == pair[j][1]):
                bb = True
                break
        if bb == False:
            return False
    return True


cases = int(input())
pair = [ [0,0] for i in range(10005)]
for i in range(cases):
    N = int(input())

    ax = 0
    ay = 0
    for j in range(N):
        cx, cy = map(int, input().split())
        pair[j][0] = cx
        pair[j][1] = cy
        ax += cx
        ay +=cy
    if ((N == 1) or resolv(ax, ay, N, pair)):
        print("yes")
    else:
        print("no")