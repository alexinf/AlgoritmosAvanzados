#!/usr/bin/python3
# coding: utf-8 


s = int(input())
for x in range(s):
	descuento_max = 0
	num_product = int(input())
	product = list(map(int, input().split()))
	product.sort(reverse = True)
	#print(product)
	for x in range(2,len(product),3):
		descuento_max += product[x]
		#print(product[x])
	print(descuento_max)
