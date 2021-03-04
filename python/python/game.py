# '---oo-------'

def change_char(s, p, r):
    return s[:p]+r+s[p+1:]

def move(moveSet, prev, nexts, current):
    if(prev >= 0 and nexts < 12):
        if(moveSet[prev] == '-' and moveSet[nexts] == 'o'):
            moveSet = change_char(moveSet, prev, 'o')
            moveSet = change_char(moveSet, current, '-')
            moveSet = change_char(moveSet, nexts, '-')
        elif (moveSet[prev] == 'o' and moveSet[nexts] == '-'):
            moveSet = change_char(moveSet, prev, '-')
            moveSet = change_char(moveSet, current, '-')
            moveSet = change_char(moveSet, nexts, 'o')
    return moveSet

def existGame(moveSet):
    size = len(moveSet)
    for position in range(size):
        prev = position - 1
        nexts = position + 1
        if (moveSet[position] != '-'):
            newMoveSet = move(moveSet, prev, nexts, position)
            if (moveSet != newMoveSet):
                return newMoveSet
    return moveSet

def playGame(moveSet):
    hasGame = True
    while hasGame:
        newMoveSet = existGame(moveSet)
        if(newMoveSet == moveSet):
            hasGame = False
        print(moveSet)
        print(newMoveSet)
        moveSet = newMoveSet
    return newMoveSet

def counto(moveSet):
    count = 0
    size = len(moveSet)
    for position in range(size):
        if (moveSet[position] != '-'):
            count += 1
    return count

# 5
games = ['---oo-------',
'-o--o-oo----',
'-o----ooo---',
'oooooooooooo',
'oooooooooo-o']

for moveSet in games:
    print('===================')
    print(counto(playGame(moveSet)))
    print('===================')

# print(playGame('oooooooooo-o'))