def kmp_table(W):
    n = len(W)
    T = [0 for _ in range(n)]
    T[0] = -1
    pos = 0

    for i in range(1, n):
        if W[i] == W[pos]:
            T[i] = T[pos]
        else:
            T[i] = pos
            pos = T[pos]
            while pos >= 0 and W[i] != W[pos]:
                pos = T[pos]
        pos += 1

    return T


print(kmp_table("rabrarera"))