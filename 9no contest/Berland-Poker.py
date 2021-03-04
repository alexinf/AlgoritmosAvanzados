
#!/usr/bin/python3
# coding: utf-8 
casos = int(input())
for x in range(casos):
    numC, numJok, jugadores = map(int, input().split())
    x = min(numJok,int(numC/jugadores))
    y = int((numJok-x+jugadores-2)/(jugadores-1))
    print(int(x-y))

# t = int(input())

# for i in range(t):
#     n, m, k = map(int, input().split())
#     ans = 0
#     d = n // k
#     for a1 in range(m + 1):
#         for a2 in range(a1 + 1):
#             if(a1 > d):
#                 continue
#             if(a1 + a2 > m):
#                 continue
#             if(a1 + (k - 1) * a2 < m):
#                 continue
#             ans = max(ans, a1 - a2)
#     print(ans)
# int

# n = numero cartas
# m = numero comodines
# k = numero de jugadores

# x = numero de comodines mano ganador

# int n, m , k; cin>> n >> m >> k;
#     int a = min(m,n/k);
#     int b = (m-a+k-2)/(k-1);
#     cout<<a-b<<endl;

# n  m  k 
# 8  3  2
# a =  min(3,4)
# a = 3
# b = (3 - 3 + 2 - 2)/(2-1)

# n  m  k 
# 4  2  4
# a =  min(2,1)
# a = 1
# b = (2 - 1 + 4 - 2)/4-1


