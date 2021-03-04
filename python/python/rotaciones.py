def rotate(input,d):
    # Lfirst = input[0 : d]
    # Lsecond = input[d :]
    Rfirst = input[0 : len(input)-d] 
    Rsecond = input[len(input)-d : ]
    return Rsecond + Rfirst

def partial(pattern):
    ret = [0]
    for i in range(1, len(pattern)):
        j = ret[i - 1]
        while j > 0 and pattern[j] != pattern[i]:
            j = ret[j - 1]
        ret.append(j + 1 if pattern[j] == pattern[i] else j)
    return ret
    
def search(T, P):
    partialVar, ret, j = partial(P), [], 0
    for i in range(len(T)):
        while j > 0 and T[i] != P[j]:
            j = partialVar[j - 1]
        if T[i] == P[j]: j += 1
        if j == len(P): 
            ret.append(i - (j - 1))
            j = 0
    return ret

def findResult(original, rotated, rotatedM):
    results = search(rotatedM, original[0:2])
    for pos in results:
        if(rotate(original, pos) == rotated):
            return pos
    return -1

size = 11
size = input() # 11
size = int(size)
original = input() # 3
# original = 'abracadabra'
rotated = input()
# rotated = 'racadabraab'
rotatedM = rotated + rotated[0]
print(findResult(original, rotated, rotatedM))