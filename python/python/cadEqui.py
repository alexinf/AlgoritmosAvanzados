# {b,n,s,u,e,o}
#  0,1,2,3,4,5

#  unos
#  3+1+5+2   / no equilibrado    n/2


#  bobo
#  0+5 + 5+0     equilibrado /2   5 = 5

#  boob
#  5+0+0+5 =10        equilibrado/2   5 =5 

#  usus 
# 3+2+3+2  = 10        equilibrado/ 2  5=5

# [0,1,2,3,4,5]
# []
#!/usr/bin/python3
# coding: utf-8
from itertools import combinations 

def todas_las_parejas(elementos):
  if len(elementos) <=2:
    return [[tuple(elementos)]]
  else:
    result = []
    diferentes = []
    for pareja in combinations(elementos, 2):
      sub_lista = elementos[:]
      sub_lista.remove(pareja[0])
      sub_lista.remove(pareja[1])
      for resto in todas_las_parejas(sub_lista):
        caso = [tuple(pareja)]
        caso.extend(resto)
        if set(caso) not in diferentes:
          print(caso)
          result.append(caso)
          #print(result)
          print("--------------------")
          diferentes.append(set(caso))
    return result

while(True):
  alpha = ([0,1,2,3,4,5])
  try:
    n, p = map(int, input().split())
  except EOFError:
    break      
  print(todas_las_parejas(alpha))


