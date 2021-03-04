from collections import Counter
from sys import stdin

while True:
    n = int(stdin.readline().strip())
    if n==0:
        break
    comb = []
    for _ in range(n):
        comb.append(tuple(sorted(map(int, stdin.readline().strip().split()))))
    kv = Counter(comb).most_common()
    max_v = kv[0][1]
    total = 0
    for k, v in kv:
        if v == max_v:
            total += max_v
        else:
            break
    print(total)