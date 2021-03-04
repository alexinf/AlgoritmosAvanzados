#!/usr/bin/python3
# coding: utf-8 
import sys

while True:
  (numSol, inf) = map(int, sys.stdin.readline().split())
  if numSol == 0 and inf == 0:
  	break
  sold = [0]*numSol
  for x in range(1,numSol+1):
  	sold[x-1]=x
  cont = 0
  for x in range(inf):
  	(lh, rh) = map(int, sys.stdin.readline().split())
  	for x in range(lh, rh + 1, 1):
  		if x in sold:
  			sold.remove(x)
  	if (len(sold) == 1):
  		if (sold[0]>1):
  			print ('* ' + str(sold[0]) )
  		else:
  			print (str(sold[0]) + ' *' )
  	elif (len(sold) > 1):
  		print (str(sold[0])+ ' ' +str(sold[1]))
  	else:
  		print ('* *')
  print ('-')

