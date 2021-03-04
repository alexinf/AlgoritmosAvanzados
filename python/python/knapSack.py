def subset_sum(numbers, target, partial=[], total=[]):
    s = sum(partial)
    if(len(total) > 2):
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
# end of function knapSack 
# 1
# 5
# 60
# 25
# 50
# 15
# 20
# 10
#print(subset_sum([25, 50, 15 ,20, 10], 41))
print(subset_sum([3, 3, 9, 8, 4, 5, 7, 10], 15))

# arr = [25, 15]
# mapDic = {}
# mapDic["25"] = 2
# mapDic["15"] = 4
# res = ""
# for x in arr:
#     res+=(str(x)+" ")
# print(res)