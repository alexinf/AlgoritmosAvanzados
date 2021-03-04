def ncr(n, r): 
    r = min(r, n-r) 
    if r == 0: return 1 
    res = 1 
    for k in range(1,r+1): 
     res = res*(n-k+1)/k
     print(res) 
    return res

print(ncr(6,4))
