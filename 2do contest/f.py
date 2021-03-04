#!/usr/bin/python3
# coding: utf-8 


def make_battle( battle, n_brothers, attak ):

    n_row = len(battle)
    n_col = len(battle[0])
    temp = [ [ battle[i][j] for j in range(n_col)] for i in range(n_row)]
    
    for i in range(n_row):
        for j in range(n_col):
            if i+1 < n_row:
                if attak[battle[i][j]] == battle[i+1][j]:
                    temp[i+1][j] = battle[i][j]            
            if i-1 >= 0:    
               if attak[battle[i][j]] == battle[i-1][j]:
                    temp[i-1][j] = battle[i][j]        
            
            if j+1 < n_col:
                if attak[battle[i][j]] == battle[i][j+1]:
                    temp[i][j+1] = battle[i][j]        
            
            if j-1 >= 0:
                if attak[battle[i][j]] == battle[i][j-1]:
                    temp[i][j-1] = battle[i][j]        
    return temp



if __name__ == '__main__':
    while True:

        line = input()
        if line == "0 0 0 0":
            break
        n, r, c, k = map(int, line.split())
        battle = []
        attak = []
        for x in range(n-1):
            attak.append(x+1)
        attak.append(0)
        for x in range(r):
            row = list(map(int, input().split()))
            battle.append(row)
        
        for x in range(k):
            battle = make_battle(battle, n, attak)
        
        for x in battle:
            print( " ".join(map(str, x)) )