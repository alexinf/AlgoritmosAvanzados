#!/ur/bin/python3
# coding: utf-8 

import sys

while True:
  (sold, inf) = map(int, sys.stdin.readline().split())
  if sold == 0 and inf == 0:
    break
  sold += 2
  left = [0] * sold
  right = [0] * sold

  for x in range(1, sold - 1):
    left[x] = x - 1
    right[x] = x + 1

  for x in range(inf):
    (lf, rt) = map(int, sys.stdin.readline().split())
    right[left[lf]] = right[rt]
    left[right[rt]] = left[lf]
    if left[lf] == 0:
      print('*', end = ' ')
    else:
      print(left[lf], end = ' ')
      
    if right[rt] == sold - 1:
      print('*')
    else:
      print(right[rt])
  print('-')