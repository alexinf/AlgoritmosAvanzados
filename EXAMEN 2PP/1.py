#from itertools import product

# variacion = list(product([0,1, 2, 3, 4, 5] , repeat = 2))
# print(variacion)

def product(rep, *args):
    pools = [tuple(pool) for pool in args] * rep
    #print(pools)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
    return (result)

rep = 2
print(list(product(rep,[0,1,2,3,4,5])))
