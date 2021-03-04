#!/usr/bin/python3
# coding: utf-8

res = []
while True:
    cad = input()
    if cad == '0':
        break
    i = curNum = 0
    curWord = ''

    for token in cad:
        if token.isdigit():
            curNum = curNum * 10 + int(token)
        elif token.isalpha():
            curWord += token
        else:
            if curWord:
                print(curWord, end='')
                res.insert(0, curWord)
            curWord = ''
            if curNum:
                print(res[curNum - 1], end='')
                res.insert(0, res.pop(curNum - 1))
            curNum = 0
            print(token, end='')

    if curWord:
        print(curWord, end='')
        res.insert(0, curWord)
    if curNum:
        print(res[curNum - 1], end='')
        res.insert(0, res.pop(curNum - 1))
    print()
