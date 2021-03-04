#!/usr/bin/python3
# coding: utf-8 

n = int(input())
animate = []
time_used = 0 
for x in range(n):
    ct , report, time_ct, time_report, lessons = map(int, input().split())
    time_used += ct*time_ct + report*time_report + lessons + 10
    animate.append(0) if time_used < 24 else animate.append(1)
    time_used = 0
for x in animate:
    print('Hotash') if x else print('Khushi')