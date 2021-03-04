#!/usr/bin/python3
# coding: utf-8 

line = input()
a, b= map(int, line.split())
sums = 0 
for x in range(a, b+1, 1):
	sums += x*x
print (sums)