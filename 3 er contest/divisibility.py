#!/usr/bin/python3
# coding: utf-8 
def divisible(div):
	num_div = []
	for x in range(div[1],div[0]):
		if x % div[1] == 0 and x % div[2]:
			num_div.append(x)
	return num_div

n = int(input())
div = []
for x in range(n):
    row = list(map(int, input().split()))
    div.append(row)
for x in range(n):
	resp = divisible(div[x])
	print (' '.join(map(str, resp)))
