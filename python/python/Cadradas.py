def readPatron (size):
    patron = []
    for x in range(0, size):
        line = input()
        patron.append(line)
    return patron

def partial(pattern):
    ret = [0]
    for i in range(1, len(pattern)):
        j = ret[i - 1]
        while j > 0 and pattern[j] != pattern[i]:
            j = ret[j - 1]
        ret.append(j + 1 if pattern[j] == pattern[i] else j)
    return ret
    
def searchKMP(T, P):
    partialVar, ret, j = partial(P), [], 0
    for i in range(len(T)):
        while j > 0 and T[i] != P[j]:
            j = partialVar[j - 1]
        if T[i] == P[j]: j += 1
        if j == len(P): 
            ret.append(i - (j - 1))
            j = 0
    return ret

def search(cuadrada, sizeC, patron, sizeP):
    firstPatron = patron[0]
    results = []
    for j in range(0, sizeC):
        patronCoincidences = searchKMP(cuadrada[j], firstPatron)
        if patronCoincidences != []:
            results.append([j, patronCoincidences])
    return results

def filterResults(results, patron, sizeP, cuadrada):
    size = len(results)
    for i in range(0, size):
        position = results[i][0]
        elements = set(results[i][1])
        for j in range(1, sizeP):
            patronCoincidences = searchKMP(cuadrada[position+j], patron[j])
            newCoincidences = elements.intersection(patronCoincidences)
            results[i][1] = newCoincidences
    return results

def printResult(result):
    sizeResult = len(result)
    coincidences = []
    totalSize = 0
    for i in range(0, sizeResult):
        setResult = result[i][1]
        size = len(setResult)
        for j in range(0, size):
            position = setResult.pop()
            totalSize +=1
            coincidences.append(str(result[i][0]) + ' ' + str(position))
    #print
    print(totalSize)
    for c in range(0, totalSize):
        print(coincidences[c])


# sizeP = input() # 2
sizeP = 2
sizeP = int(sizeP)
# patron = readPatron(sizeP)
patron = ["HI", "JK"]
# sizeC = input() # 6
sizeC = 6
sizeC = int(sizeC)
# cuadrada = readPatron(sizeC)
cuadrada = 
[
"ABHIHI",
"HIJKJK",
"JKTESR",
"JCNHIY",
"HIUJKR",
"JKUTYR"]
results = search(cuadrada, sizeC, patron, sizeP)
results = filterResults(results, patron, sizeP, cuadrada)
printResult(results)
# 2
# HI
# JK
# 6
# ["ABHIDE",
# "HIJKRD",
# "JKTESR",
# "JCNHIY",
# "JDUJKR",
# "HDUTYR"]
