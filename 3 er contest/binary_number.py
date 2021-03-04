
def greater_than(num1, num2):
	resp = 0
	if(int(num1, 2) > int(num2, 2)):
		resp = 1
	return resp	

def addition(num1, num2):
	return ('addition')

def subtraction(num1, num2):
	return ('subtraction')

def multiplication(num1, num2):
	return ('multiplication')

def division(num1, num2):
	return ('division')

n = input()
answers = []
for x in range(int(n, 2)):
	operation, num1 , num2 = (input().split())
	#print (operation, num1, num2)
	solution = {
		'0': greater_than(num1, num2),
		'1': addition(num1, num2),
		'10': subtraction(num1, num2),
		'11': multiplication(num1, num2),
		'100': division(num1, num2)
	}
	answers.append(solution.get(operation))

for x in answers:
	print (x)	
