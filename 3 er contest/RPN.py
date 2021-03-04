#!/usr/bin/python3
# coding: utf-8 

def check(row):
	resp = 0
	num = [k for k in row if not (k in "+*-/")]
	if (len(num)-1 == len(row)-len(num)):
		resp = 1
	return resp

def solution(row):
	aux = []
	segundo = 0
	primero = 0
	resp = 0
	for x in row:
		if (x in "+*-/"):
			segundo = aux.pop()
			primero = aux.pop()
			operation = {
				'/': primero / segundo,
				'*': primero * segundo,
				'-': primero - segundo,
				'+': primero + segundo
			}
			aux.append(operation.get(x))			
		else:
			aux.append(float(x))

		segundo = 0 
		primero = 0
	resp = aux.pop()
	return resp

while True:
	try:
		row = list(input().split())
	except EOFError:
		break
	check_problem = check(row)
	if(check_problem):
		print("{0:.4f}".format(solution(row)))
	else:
		print('ERROR')
