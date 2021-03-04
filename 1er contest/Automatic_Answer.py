#!/usr/bin/python3
# coding: utf-8 
import sys

ini = sys.stdin.readline()	

for x in range(int(ini)):
	a = int(sys.stdin.readline())
	c = abs(int(((((((((a*567)/9)+7492)*235)/47)-498)))))
	print(abs(int((c/10)%10)))
