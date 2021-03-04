from collections import Counter
from sys import stdin

if __name__ == "__main__":
    while True:
        n = int(stdin.readline().strip())
        if n==0:
            break
        comb = []
        for _ in range(n):
            comb.append(tuple(sorted(map(int, stdin.readline().strip().split()))))
        print(comb)
        kv = Counter(comb).most_common()
        print(kv)
        max_v = kv[0][1]
        print(max_v)
        total = 0
        for k, v in kv:
            if v == max_v:
                total += max_v
            else:
                break
        print(total)