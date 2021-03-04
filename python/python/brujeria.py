import re

def filterMin(caramels, minSize):
    result = []
    for item in caramels:
        result.append(item)
    return result

def missingCandies(caramels, totalSize, mapDic) :
    result = subset_sum(caramels, totalSize)
    printResult = "Brian, Kevin faltan "
    if (len(result)>1):
        printResult+="caramelos "
    else:
        res = ""
        for x in result[0]:
            index = str(x)
            res+=(mapDic[index]+" ")
        printResult+=res
    printResult+="!!!"
    print(printResult)

def subset_sum(numbers, target, partial=[], total=[]):
    s = sum(partial)
    if(len(total) > 1):
        return
    if s == target:
        total.append(partial)
        return partial
        # print("sum(%s)=%s" % (partial, target))
    if s >= target:
        return []
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, partial + [n])
    return total

cases = input() # 3
cases = int(cases)
for x in range(0, cases):
    size = input()
    size = int(size)
    totalSize = input()
    totalSize = int(totalSize)
    caramels = []
    total = 0
    mapDic = {}
    for x in range(0, size):
        caramel = input()
        mapDic[caramel] = str(x+1)
        caramel = int(caramel)
        total += caramel
        caramels.append(caramel)
    if (totalSize == total):
        print("-")
    else:
        restSize = total - totalSize
        caramels = filterMin(caramels, restSize)
        missingCandies(caramels, restSize, mapDic)