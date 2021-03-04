

casos = int(input())

for c in range(casos):
	tam = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	a_a = [None]*len(a)
	b_b = [None]*len(b)
	a_a [0] = a [0]
	b_b [0] = b [0]
	for x in range(tam+1,1):
		a_a [x] = 0
		for y in range (x):
			if a[y]<a[x]:
				a_a [x] = max(a_a[y],a_a[x])
			else:
				b_b [x] = max(b_b[x],b_b[y])
		a_a[x] += b[x]
		b_bp[x]+= b[x]

	Increasing = 0
	Decreasing = 0
	for z in range(tam):
		Increasing = max(Increasing,int(a_a[z]))
		Decreasing = max(Decreasing,int(b_b[z]))
	if Increasing >= Decreasing:
		print('Case '+str(c) +'.'+'Increasing '+ str(Increasing)+'.'+ 'Decreasing '+str(Decreasing)+'.')
	else:
		print('Case '+str(c) +'.'+'Increasing '+ str(Decreasing)+'.'+ 'Decreasing '+str(Increasing)+'.')



