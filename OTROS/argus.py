#!/usr/bin/python
# coding: utf-8

from sys import stdin

class Register():
    def __init__(self, id, time, period):
        self.id = id
        self.time = time
        self.period = period

    def __gt__(self, register):

        return  self.id > register.id if self.time == register.time else self.time > register.time


if __name__ == "__main__":
    
    register = []

    while True:
        line = stdin.readline().strip()
        if line == '#':
            register = sorted(register)
            break
        id, time = map(int, line.split()[1:])
        register.append(Register(id, time, time))

    k = int(stdin.readline())

    while k > 0:
        bb = register[0]
        
        print(bb.id)
        bb.time += bb.period
        register.pop(0)
        register.append(bb)
        register = sorted(register)

        k-=1


