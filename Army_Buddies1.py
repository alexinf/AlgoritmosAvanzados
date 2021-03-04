#!/usr/bin/python3
# coding: utf-8 

import sys

while True:
  (s, b) = map(int, sys.stdin.readline().split())
  if s == 0 and b == 0: break
  lf = [0] * (s + 2)
  rf = [0] * (s + 2)

  for i in range(1, s + 1):
    lf[i] = i - 1
    rf[i] = i + 1
  for i in range(b):
    (lh, rh) = map(int, sys.stdin.readline().split())
    rf[lf[lh]] = rf[rh]
    lf[rf[rh]] = lf[lh]
    if lf[lh] == 0:
      print('*', end = ' ')
    else:
      print(lf[lh], end = ' ')
      
    if rf[rh] == s + 1:
      print('*')
    else:
      print(rf[rh])
  print('-')