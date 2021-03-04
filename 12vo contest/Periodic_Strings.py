#!/usr/bin/python3
# coding: utf-8

n=int(input()) 

while(n):
    input()
    s=input()
    res=-1
    tamCad=int(len(s)/2)
    recoridoCad=0
    while(recoridoCad<=tamCad):
        subCad=s[:recoridoCad]
        numRep=s.count(subCad)
        result=numRep*recoridoCad
        if(result == len(s)):
            res=recoridoCad
            break
        recoridoCad +=1

    if (res == -1):
        res=len(s)
    print(res)
    n -= 1
    if (n!=0):
        print()