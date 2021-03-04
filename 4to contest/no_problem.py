#!/usr/bin/python3
# coding: utf-8 

case = 1
state = 1
while(state):
	pro = []
	req = []
	s = int(input())
	if(s<0):
		break
	pro = list(map(int, input().split()))
	req = list(map(int, input().split()))
	print ('Case ' + str(state) + ':' )
	for x in range(12):
		if(req[x] <= s):
			print('No problem! :D')
			s -=req[x]
		else:
			print('No problem. :(')
		s += pro[x]
	state +=1
	