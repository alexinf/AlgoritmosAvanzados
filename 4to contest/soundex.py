#!/usr/bin/python3
# coding: utf-8 

tones = ['BFPV','CGJKQSXZ','DT','L','MN','R', 'AEIOUHWY']
while(True):
	try:
		note = input()
	except EOFError:
		break
	resp = ''
	b = 0
	for x in note:
		for y in range(len(tones)-1):
			if (x in tones[y]):
				if( b != y+1):
					resp +=str(y+1) 
					b = y+1
		if(x in tones[6]):
			b = 0
	print(resp)

