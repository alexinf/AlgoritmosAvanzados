# Python3 program to find 
# the number of islands using 
# Disjoint Set data structure. 

# Class to represent 
# Disjoint Set Data structure 
from statistics import mode


class DisjointUnionSets: 
    def __init__(self, n): 
        self.rank = [0] * n 
        self.parent = [0] * n 
        self.n = n 
        self.makeSet() 

    def makeSet(self): 
        
        # Initially, all elements are in their 
        # own set. 
        for i in range(self.n): 
            self.parent[i] = i 

    # Finds the representative of the set that x 
    # is an element of 
    def find(self, x): 
        if (self.parent[x] != x): 

            # if x is not the parent of itself, 
            # then x is not the representative of 
            # its set. 
            # so we recursively call Find on its parent 
            # and move i's node directly under the 
            # representative of this set 
            # compresion de caminos
            self.parent[x] = self.find(self.parent[x]) 
            return self.parent[x]
        return x 

    # Unites the set that includes x and 
    # the set that includes y 
    def Union(self, x, y): 
        
        # Find the representatives(or the root nodes) 
        # for x an y 
        xRoot = self.find(x) 
        yRoot = self.find(y) 

        # Elements are in the same set, 
        # no need to unite anything. 
        if xRoot == yRoot: 
            return

        # If x's rank is less than y's rank 
        # Then move x under y so that depth of tree 
        # remains less 
        if self.rank[xRoot] < self.rank[yRoot]: 
            self.parent[xRoot] = yRoot 

        # Else if y's rank is less than x's rank 
        # Then move y under x so that depth of tree 
        # remains less 
        elif self.rank[yRoot] < self.rank[xRoot]: 
            self.parent[yRoot] = xRoot 

        else: 
            
            # Else if their ranks are the same 
            # Then move y under x (doesn't matter 
            # which one goes where) 
            self.parent[yRoot] = xRoot 

            # And increment the result tree's 
            # rank by 1 
            self.rank[xRoot] = self.rank[xRoot] + 1

# Returns number of islands in a[][] 
def countIslands(a): 
    n = len(a) 
    m = len(a[0]) 

    dus = DisjointUnionSets(n * m) 

    # The following loop checks for its neighbours 
    # and unites the indexes if both are 1. 
    for j in range(0, n): 
        for k in range(0, m): 

            # If cell is 0, nothing to do 
            if a[j][k] == 0: 
                continue

            # Check all 8 neighbours and do a Union 
            # with neighbour's set if neighbour is 
            # also 1 
            if j + 1 < n and a[j + 1][k] == 1: 
                dus.Union(j * (m) + k, 
                        (j + 1) * (m) + k) 
            if j - 1 >= 0 and a[j - 1][k] == 1: 
                dus.Union(j * (m) + k, 
                        (j - 1) * (m) + k) 
            if k + 1 < m and a[j][k + 1] == 1: 
                dus.Union(j * (m) + k, 
                        (j) * (m) + k + 1) 
            if k - 1 >= 0 and a[j][k - 1] == 1: 
                dus.Union(j * (m) + k, 
                        (j) * (m) + k - 1) 
            if (j + 1 < n and k + 1 < m and
                    a[j + 1][k + 1] == 1): 
                dus.Union(j * (m) + k, (j + 1) *
                            (m) + k + 1) 
            if (j + 1 < n and k - 1 >= 0 and
                    a[j + 1][k - 1] == 1): 
                dus.Union(j * m + k, (j + 1) *
                            (m) + k - 1) 
            if (j - 1 >= 0 and k + 1 < m and
                    a[j - 1][k + 1] == 1): 
                dus.Union(j * m + k, (j - 1) *
                            m + k + 1) 
            if (j - 1 >= 0 and k - 1 >= 0 and
                    a[j - 1][k - 1] == 1): 
                dus.Union(j * m + k, (j - 1) *
                            m + k - 1) 

    # Array to note down frequency of each set 
    c = [0] * (n * m) 
    numberOfIslands = 0
    for j in range(n): 
        for k in range(n): 
            if a[j][k] == 1: 
                x = dus.find(j * m + k) 
                
                # If frequency of set is 0, 
                # increment numberOfIslands 
                if c[x] == 0: 
                    numberOfIslands += 1
                    c[x] += 1
                else: 
                    c[x] += 1
    print(dus.parent)
    #print(mode(dus.parent))
    # print(dus.rank)
    return numberOfIslands 

# Driver Code 
a = [[1, 1, 0, 0, 0], 
    [0, 1, 1, 0, 1], 
    [1, 0, 0, 1, 1], 
    [0, 0, 0, 0, 0], 
    [1, 0, 1, 0, 1]] 
print("Number of Islands is:", countIslands(a))


# This code is contributed by ankush_953 
