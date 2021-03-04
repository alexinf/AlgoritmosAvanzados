#!/usr/bin/python3
# coding: utf-8 


def make_battle( battle, n_brothers ):

    n_row = len(battle)
    n_col = len(battle[0])
    temp = [ [ battle[i][j] for j in range(n_col)] for i in range(n_row)]
    
    for i in range(n_row):
        for j in range(n_col):
            if i+1 < n_row:
            
                if battle[i][j] == n_brothers-1:
                    if battle[i+1][j] == 0:
                        temp[i+1][j] = battle[i][j]
                else:
                    if battle[i+1][j] -1 == battle[i][j]:
                        temp[i+1][j] = battle[i][j]
            
            if i-1 >= 0:    
                if battle[i][j] == n_brothers-1:
                    if battle[i-1][j] == 0:
                        temp[i-1][j] = battle[i][j]
                else:
                    if battle[i-1][j] -1 == battle[i][j]:
                        temp[i-1][j] = battle[i][j]
            
            if j+1 < n_col:
                if battle[i][j] == n_brothers-1:
                    if battle[i][j+1] == 0:
                        temp[i][j+1] = battle[i][j]
                else:
                    if battle[i][j+1] -1 == battle[i][j]:
                        temp[i][j+1] = battle[i][j]
            
            if j-1 >= 0:
                if battle[i][j] == n_brothers-1:
                    if battle[i][j-1] == 0:
                        temp[i][j-1] = battle[i][j]
                else:
                    if battle[i][j-1] -1 == battle[i][j]:
                        temp[i][j-1] = battle[i][j]
    return temp



if __name__ == '__main__':
    while True:

        line = input()
        if line == "0 0 0 0":
            break
        n, r, c, k = map(int, line.split())
        battle = []
        for x in range(r):
            row = list(map(int, input().split()))
            battle.append(row)
        
        for x in range(k):
            battle = make_battle(battle, n)
        
        for x in battle:
            print( ' '.join(map(str, x)) )