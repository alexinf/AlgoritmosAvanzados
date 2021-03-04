b =  [[22,56,33] , [21,58,33], [20,51,39]]
 
for i in range(0, 3):
    for j in range(0, 3):
        valor = b[i][j]
        if valor <= 50:
            b[i][j] = 0
        else:
            b[i][j] = 1
 
print (b)