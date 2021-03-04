from collections import defaultdict
from heapq import *
import re

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)

            if v1 == t: return re.sub("[()']", "", str(path))
            # if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))
    return float("inf")

def loadweights(ways, size):
    weights = {}
    for index in range(0, size-1):
        currentWay = str(ways[index])
        NextWay = str(ways[index+1])
        if (weights.get(NextWay) == None):
            weights[currentWay] = 1
        else:
            weights[currentWay] = 2
    return defBuildEdges(weights, ways, size)

def defBuildEdges(weights, ways, size):
    edges = []
    for x in range(0, size-1):
        current = str(ways[x])
        nextEdge = str(ways[x+1])
        edges.append((current, nextEdge, weights[current]))
    return edges

def printResult(ways, size):
    edges = loadweights(ways, size)
    if (ways[0] == ways[size-1]):
        print("Camila esto no va a dar")
    else:
        toPrint = ""
        result = dijkstra(edges, str(ways[0]), str(ways[size-1]))
        result = result.split(',')
        resultSize = len(result)
        for x in range(2, resultSize+1):
            way = result[resultSize-x].strip()
            if(resultSize-x == 0):
                toPrint+=way
            else:
                toPrint+=way + ' '
        print(toPrint)
cases = input() # 3
cases = int(cases)
# cases = 3
for x in range(0, cases):
    size = input()
    size = int(size)
    ways = input()
    printResult(ways.split(' '), size)

# size = 9
# ways = [1, 2, 7, 3, 2, 8, 4, 8, 5]
# print('Hi, %s.' % name)

# 3
# 9
# 1 2 7 3 2 8 4 8 5
# 3
# 1 2 1
# 5
# 1 2 3 4 2   
