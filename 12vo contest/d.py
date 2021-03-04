#!/usr/bin/python3
# coding: utf-8

import sys

def lcs(line1, line2):
    len1 = len(line1)
    len2 = len(line2)
    length = [[0] * len2 for _ in range(len1)]

    for idx in range(1, len1):
        for jdx in range(1, len2):
            if line1[idx] == line2[jdx]:
                length[idx][jdx] = length[idx - 1][jdx - 1] + 1
            else:
                length[idx][jdx] = max(length[idx - 1][jdx], length[idx][jdx - 1])

    lcs_length = length[len1 - 1][len2 - 1]
    idx = len1 - 1
    jdx = len2 - 1
    lcs_words = [[] for _ in range(lcs_length)]
    kdx = lcs_length - 1

    while kdx >= 0:
        if line1[idx] == line2[jdx]:
            lcs_words[kdx] = line1[idx]
            kdx -= 1
            idx -= 1
            jdx -= 1
        else:
            if length[idx][jdx - 1] > length[idx - 1][jdx]:
                jdx -= 1
            else:
                idx -= 1

    return lcs_length, lcs_words



recs = iter(sys.stdin.readlines())
text1 = []
text2 = []
case = 0
while True:
    try:
        data = next(recs).split()
        if data[0] == '#':
            case = (case + 1) % 2

            if case == 0:
                text1.insert(0, "")
                text2.insert(0, "")
                length, words = lcs(text1, text2)
                print(" ".join(words))
                text1.clear()
                text2.clear()
            continue

        if case == 0:
            text1.extend(data)
        else:
            text2.extend(data)

    except (StopIteration):
        break