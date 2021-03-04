#!/usr/bin/python
# coding: utf-8

from collections import Counter
from sys import stdin

if __name__=="__main__":
    for _ in range(int(stdin.readline().strip())):
        list_stamp_friends = []

        exhibitions = []
        for i in range(int(stdin.readline().strip())):
            line = list(set(stdin.readline().strip().split()[1:]))
            list_stamp_friends.append(line)

            for stamp in line:
                exhibitions.append(stamp)
        
        a = list(filter( lambda x: x[1] == 1, Counter(exhibitions).most_common()))
        percent = 100/len(a) if len(a) > 0 else 0
        final_value = []
        for i in list_stamp_friends:
            valor = len(set(i) & set([ j[0] for j in a])) * percent
            final_value.append("{0:.6f}".format(valor)+'%')
        # print(percent)
        # print(a)
        # print(list_stamp_friends)
        print(f'Case {_+1}: {" ".join(final_value)}')
        
