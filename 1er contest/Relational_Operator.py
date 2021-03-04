#!/usr/bin/python3
# coding: utf-8 
import sys

ini = sys.stdin.readline()	
dic = ['=', '<', '>']
for x in range(int(ini)):
	a, b= map(int, sys.stdin.readline().split())
	if (a == b):
		c = 0
	elif (a < b):
		c = 1
	else:
		c = 2
	print(dic[c])
