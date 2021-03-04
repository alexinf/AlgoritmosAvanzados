#!/usr/bin/python3
# coding: utf-8 
qd = [1]*65
for x in range(4,62):
	 qd[x] = qd[x-1] + qd[x-2] + qd[x-3];
case = 1
while True:
	N = int(input())
	if N == 0:
		break
	print("Case "+ str(case) + ": " + str(qd[N]) )
	case +=1

