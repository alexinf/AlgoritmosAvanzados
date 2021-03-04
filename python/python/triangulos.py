import math

class Point:
    def __init__(self, valuex, valuey):
        self.x = valuex
        self.y = valuey
    
    def sizeLine(self, point):
        x = abs(self.x - point.x)
        y = abs(self.y - point.y)
        return math.sqrt(x**2 + y**2)

    def getMediumPoint(self, point):
        x = abs(self.x + point.x)/2
        y = abs(self.y - point.y)/2
        return Point(x,y)

def calculateTriArea(base, h):
    return (base*h)/2

def getH(line, baseLine):
    newBase = baseLine/2
    sum = abs(newBase**2 - line**2)
    return math.sqrt(sum)

def readPoints(points):
    result = []
    values = points.split(' ')
    for i in range(0, 4):
        pos = i*2
        result.append(Point(float(values[pos]),float(values[pos+1])))
    return result

def lines(points):
    ab = points[0].sizeLine(points[1])
    ac = points[0].sizeLine(points[2])
    bc = points[1].sizeLine(points[2])
    pointCirle = points[1].getMediumPoint(points[2])
    circleR = points[3].sizeLine(pointCirle)
    

# cases = input() # 2
# cases = int(cases)
# cases = 2
# for x in range(0, cases):
#     points = input()
    
read = readPoints('1.00 3.00 5.00 7.00 7.00 0.00 4.09 3.50')
lines(read)
print(read)
# 2
# 1.00 3.00 5.00 7.00 7.00 0.00 4.09 3.50
# 2.00 4.00 5.00 9.00 7.00 3.00 4.57 5.13
